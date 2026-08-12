import inspect
from functools import wraps

from app import app

def inject(func):
    """Injects dependencies into the function."""

    @wraps(func)
    def function_wrapper(*args, **kwargs):
        arguments = inspect.getfullargspec(func)

        for key, val in arguments.annotations.items():
            # skip "return" annotation
            if key == "return":
                continue

            # Prevent overwriting existing kwargs
            if key in kwargs:
                continue

            to_inject = app.injector[val.__name__]

            if to_inject is not None:
                kwargs[key] = to_inject
        return func(*args, **kwargs)
    return function_wrapper