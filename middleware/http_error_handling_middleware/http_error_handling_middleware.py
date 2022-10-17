from django.http import JsonResponse

from common.http_errors import HttpError, InternalServerError


class HttpErrorHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_exception(_request, exception):
        if not isinstance(exception, HttpError):
            exception = InternalServerError()

        response_body = {
            "status": exception.status,
            "data": {
                "status": exception.status,
                "message": exception.message
            }
        }

        if exception.data is not None:
            response_body["data"]["content"] = exception.data

        return JsonResponse(
            status=exception.status,
            data=response_body
        )
