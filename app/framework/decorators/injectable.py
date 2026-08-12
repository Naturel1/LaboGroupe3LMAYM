from app.framework.injector import DependencyConfig, Scope, register_dependency


def injectable(cls: None, *, base = None, scope: Scope = Scope.SINGLETON):
    """Declares a class as injectable."""
    def decorate(target):
        register_dependency(DependencyConfig(base or target, target, scope))

        return target

    if cls is None:
        return decorate

    return decorate(cls)
