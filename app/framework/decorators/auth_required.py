import inspect
from functools import wraps

from flask import flash, redirect, url_for, request

from app.dtos.user_dto import UserDTO
from app.framework.decorators.inject import inject
from app.services.auth_service import AuthService


def auth_required(level=None, or_is_current_user=False):
    """Decorator to verify the role or user propriety.
    - @auth_required() : user must be logged in
    - @auth_required(level="ADMIN) : user must be admin
    - @auth_required(or_is_current_user=True) : Route is property of user or is admin
    """

    def auth_required_decorator(func):
        if or_is_current_user:
            if "user_id" not in inspect.signature(func).parameters:
                raise ValueError("The function must have a 'user_id' parameter")

            if level == "USER":
                raise ValueError("User level is not supported with or_is_current_user")

        @wraps(func)
        @inject
        def function_wrapper(*args, auth_service: AuthService, **kwargs):
            current_user: UserDTO | None = auth_service.get_current_user()

            if current_user is None:
                flash("You must be logged in to access this page", "warning")
                return redirect(url_for("login", next=request.path))

            roles = current_user.role_names()

            if "ADMIN" in roles:
                return func(*args, **kwargs)

            if level is not None and level in roles:
                return func(*args, **kwargs)

            if or_is_current_user and current_user.user_id == kwargs.get("user_id"):
                return func(*args, **kwargs)

            if level is None and not or_is_current_user:
                return func(*args, **kwargs)

            flash("You don't have the required permission to access this page", "danger")
            return redirect(url_for("index"))

        return function_wrapper

    return auth_required_decorator
