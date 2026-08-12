from enum import Enum

from flask import Flask, g, has_app_context


class Scope(Enum):
    """Lifespan of the dependency."""

    # Only one instance of the dependency is created.
    SINGLETON = 1
    # A new instance is created for each request.
    SCOPED = 2
    # A new instance is created for each function call.
    TRANSIENT = 3


class DependencyConfig:
    """Configuration for a dependency.

    - base: Base class or interface for the dependency.
    - implement: Concrete class or implementation of the dependency.
    - scope: Lifespan of the dependency.
    """

    def __init__(self, base, implement, scope: Scope):
        self.base = base
        self.implement = implement
        self.scope = scope


class ContainerConfig:
    """Configuration for the dependency injection container."""

    def __init__(self):
        self.__config = {}

    def bind(self, dependency: DependencyConfig):
        self.__config[dependency.base.__name__] = dependency

    def get(self, dep_name) -> DependencyConfig | None:
        return self.__config.get(dep_name)

__dependencies: dict[str, DependencyConfig] = {}


def register_dependency(dependency: DependencyConfig):
    """Register a dependency in the dependency injection container."""
    __dependencies[dependency.base.__name__] = dependency


def registered_dependencies() -> list[DependencyConfig]:
    """Get a list of all registered dependencies."""
    return list(__dependencies.values())


class Injector:
    """Dependency injection container."""

    def __init__(self, app: Flask, config=None):
        self.__config = ContainerConfig()

        for dependency in registered_dependencies():
            self.__config.bind(dependency)

        if config is not None:
            config(self.__config)

        app.injector = self

        self.__singleton = {}

    def __getitem__(self, item):
        """Able the syntaxe injector['UserService']."""
        dep = self.__config.get(item)

        if dep is None:
            return None

        if dep.scope == Scope.SINGLETON:
            return self.__get_singleton(dep)

        if dep.scope is Scope.SCOPED:
            return self.__get_scoped(dep)

        return self.__get_transient(dep)

    def __get_singleton(self, dependency: DependencyConfig):
        if self.__singleton.get(dependency.base.__name__) is None:
            self.__singleton[dependency.base.__name__] = dependency.implement()

        return self.__singleton[dependency.base.__name__]

    def __get_scoped(self, dependency: DependencyConfig):
        if not has_app_context():
            return self.__get_transient(dependency)

        scoped = g.setdefault("_injector_scoped", {})

        if scoped.get(dependency.base.__name__) is None:
            scoped[dependency.base.__name__] = dependency.implement()

        return scoped[dependency.base.__name__]

    def __get_transient(self, dependency: DependencyConfig):
        return dependency.implement()