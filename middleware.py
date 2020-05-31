import json
import traceback
import logging

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from my_auth.exceptions import InnerException


logger = logging.getLogger(__name__)


class ExceptionBoxMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if not issubclass(exception.__class__, InnerException):
            return None
        ret_json = {
            'code': exception.code,
            'message': getattr(exception, 'msg', 'error'),
            'result': False,
            'data': None
        }
        response = JsonResponse(ret_json)
        _logger = logger.error if response.status_code >= 500 else logger.warning
        _logger('status_code->{status_code}, error_code->{code}, url->{url}, '
                'method->{method}, param->{param}, '
                'body->{body}，traceback->{traceback}'.format(
            status_code=response.status_code, code=ret_json['code'], url=request.path,
            method=request.method, param=json.dumps(getattr(request, request.method, {})),
            body=request.body, traceback=traceback.format_exc()
        ))
        return response
