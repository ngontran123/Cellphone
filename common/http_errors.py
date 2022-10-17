from typing import Dict


class HttpError(Exception):
    def __init__(self, *, status: int, message: str, data: Dict = None):
        self.status = status
        self.message = message
        self.data = data


class BadRequestError(HttpError):
    def __init__(self, *, message='Bad request', data=None):
        super().__init__(status=400, message=message, data=data)


class UnauthorizedError(HttpError):
    def __init__(self, *, message='Unauthorized', data=None):
        super().__init__(status=401, message=message, data=data)


class ForbiddenError(HttpError):
    def __init__(self, *, message='Forbidden', data=None):
        super().__init__(status=403, message=message, data=data)


class NotFoundError(HttpError):
    def __init__(self, *, message='Not found', data=None):
        super().__init__(status=404, message=message, data=data)


class ConflictError(HttpError):
    def __init__(self, *, message='Conflict', data=None):
        super().__init__(status=409, message=message, data=data)


class InternalServerError(HttpError):
    def __init__(self):
        super().__init__(status=500, message='Internal server error')
