from django.views import View
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

from .models import UserInfo
from .exceptions import UserNotExistsException, UserPasswordError, UserAlreadyExistsException


class LoginView(View):
    """
    #group  认证
    #name   登录
    #desc   登录
    #param  username     <str>     登录账号
    #param  password    <str>    登录密码

    #return user_id <int>  用户ID
    #example
    {
        "code": 0,
        "msg": "登录成功",
        "data": {
            "user_id": 1,
    }
    """
    # @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.POST
        username = data.get('username')
        user = UserInfo.objects.filter(username=username).first()
        if not user:
            raise UserNotExistsException()

        password = data.get('password')
        print('debug password:', password)
        if not check_password(password, user.password):
            raise UserPasswordError()

        return JsonResponse({
            'user_id': user.id,
        })


class RegisterView(View):
    """
    #group  认证
    #name   注册
    #desc   注册
    #param  username     <str>     登录账号
    #param  password    <str>    登录密码

    #return user_id <int>  用户ID
    #example
    {
        "code": 0,
        "msg": "注册成功",
        "data": {
            "user_id": 1,
            "username": "18911067807",
            "token": ".eJwFwbkVRCEIAMBejA04BWrZt4Ec9l_Cn_nhXmuFcpWGvDUhcznWvmkVXjl0"
    }
    """

    def post(self, request, *args, **kwargs):
        data = request.POST
        username = data.get('username')
        user = UserInfo.objects.filter(username=username).first()
        if user:
            raise UserAlreadyExistsException()

        user = UserInfo.objects.create(**data)

        return JsonResponse({
            'user_id': user.id,
        })
