class AppException(Exception):
    """Base application exception"""
    pass


class NotFoundError(AppException):
    pass


class ConflictError(AppException):
    pass