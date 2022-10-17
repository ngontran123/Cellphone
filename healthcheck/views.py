from django.http import HttpRequest

from common.http_errors import BadRequestError


def index(_req: HttpRequest):
    raise BadRequestError(
        message="Hello World",
        data={
            "name": 'Quang Pham'
        }
    )
