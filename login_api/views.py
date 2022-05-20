import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
import jwt, datetime
from .models import User
from .sj_auth import uis_api

class LoginView(APIView):
    def post(selfself, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None: # DB에 아이디가 없는경우
            user_info = uis_api(username, password) # 세종대 학사 홈페이지에 로그인시킴

            if user_info["result"] is False: # 세종대 로그인에 실패한 경우
                raise AuthenticationFailed('Check Sejong id!')

            user = User.objects.create_user(username, user_info['email'], password)
            user.first_name = user_info["first_name"]
            user.major = user_info["major"]
            user.phone_number = user_info["phone_number"]
            user.save()

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticatied!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticatied!')

        user = User.objects.filter(id = payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

'''
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
'''