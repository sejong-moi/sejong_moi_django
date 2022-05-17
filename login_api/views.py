import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from .sj_auth import uis_api


@api_view(['GET'])
def helloApi(request):
    return Response("hello world")

@api_view(['POST'])
def login(request):
    if request.method == "POST":
        username = json.loads(request.body.decode())["username"]
        password = json.loads(request.body.decode())["password"]
        print(username, password)
        user_info = uis_api(username, password)

        if user_info["result"] is True:
            print("로그인 성공")
            print(user_info)
            if username not in User.objects.values_list("username", flat=True):
                print("처음 로그인")
                first_name = user_info["first_name"]
                major = user_info["major"]
                phone_number = user_info["phone_number"]
                email = user_info["email"]
                print(password)
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.major = major
                user.phone_number = phone_number
                user.save()
                return Response("True")

            else:
                print("이미 가입됨")
                user = authenticate(username=username, password=password)
                print(user.is_authenticated)
                if user is not None:
                    print("인증성공")
                    return Response("True")
                else:
                    print("인증 실패")
                    return Response("False")

        else:
            print("로그인 실패")
            return Response("False")


    return Response("False")