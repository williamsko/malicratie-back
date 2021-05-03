
import json
from tastypie.exceptions import TastypieError
from tastypie.http import HttpApplicationError


class CustomBadRequest(TastypieError):
    """
    This exception is used to interrupt the flow of processing to immediately
    return a custom HttpResponse.
    """

    def __init__(self,status,msg):
        self._response = {
            "status" : status,
            "msg": msg
            }

    @property
    def response(self):
        return HttpApplicationError(
            json.dumps(self._response),
            content_type='application/json')
