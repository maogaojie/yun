from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password
from userapp.serializer import *
# from fileapp.serializer import
from userapp.models import User, UserInfo
from fileapp.models import File
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired
from fature.settings import SECRET_KEY, HOME_PATH
import os
from django.http import Http404

# Create your views here.

itsdangerous_serializer = TimedJSONWebSignatureSerializer(SECRET_KEY, 120)


class Signup(APIView):
    '''
    用户注册，密码加盐 hash
    生成用户目录
    '''
    def post(self, request):
        data = request.data
        print(data)
        oc_ser = UserSignUpSerializer(data=request.data)
        if oc_ser.is_valid():
            oc_ser.save()
            user = User.objects.filter(account=data['account']).first()
            datas = {'user_id':user.id,'is_active':True,'size':8388608,'used':0,'path':'/root/yun/'}
            sto = StorageSerializerAPIView(data = datas)
            if sto.is_valid():
                sto.save()
                code = 0
                message = 'Success'

            else:
                message = oc_ser.errors
                code = 4002
                message = message
            return Response({
                'code': code,
                'message': message,
            })
        else:
            message = oc_ser.errors
            code = 4001
        return Response({
            'code': code,
            'message': message,
        })


class Signin(APIView):
    def post(self, request):
        data = {}
        print(request.data)
        account = request.data.get('account')
        password = request.data.get('password')
        try:
            user = User.objects.get(
                account=account
            )
        except:
            data['code'] = 4001
            data['message'] = 'Have no account'
        else:
            if not check_password(password, user.password):
                data['code'] = 4001
                data['message'] = 'Password check Failed'
            else:
                request.session['user_id'] = user.id  # 添加session -> COOCIE: sessionID
                data['token'] = itsdangerous_serializer.dumps(
                    {'user_id': user.id}).decode()  # 返回Token
                data['code'] = 0
                data['message'] = 'Success'
        return Response(data)


class Signout(APIView):
    def get(self, request):
        data = {}
        del request.session['user_id']
        data['code'] = 0
        return Response(data)

class Verify(APIView):
    def post(self, request):
        data = {}
        token = request.data['token']
        try:
            itsdangerous_serializer.loads(token)
        except:
            data['code'] = 4001
        else:
            data['code'] = 0
        return Response(data)
