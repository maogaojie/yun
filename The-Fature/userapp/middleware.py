from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from fature.settings import SECRET_KEY, HOME_PATH
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired

itsdangerous_serializer = TimedJSONWebSignatureSerializer(SECRET_KEY, 120)

class UserMiddleware(MiddlewareMixin):
    pass
