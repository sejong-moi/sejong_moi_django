import json

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Club, Category
from login_api.models import User, Interesting_Club
from .serializers import ClubSerializer


# Create your views here.

@api_view(['GET'])
def club(request, name):
    if request.method == 'GET':
        club = Club.objects.get(name=name)
        serializers = ClubSerializer(club)
        interested = serializers.data['interested']
        interested_username = []
        for id in interested:
            interested_username.append(User.objects.get(id=id).username)
        print(interested_username)
        response = Response(data=serializers.data)
        response.data['interested_username'] = interested_username

        return response


@api_view(['GET'])
def list(request):
    if request.method == 'GET':
        queryset = Club.objects.all()
        serializers = ClubSerializer(queryset, many=True)
        return Response(serializers.data)

# 공연
@api_view(['GET'])
def list_show(request):
    if request.method == 'GET':
        queryset = set(Club.objects.filter(category__club__category='1'))
        serializers = ClubSerializer(queryset, many=True)
        return Response(serializers.data)

# 문화
@api_view(['GET'])
def list_cluture(request):
    if request.method == 'GET':
        queryset = set(Club.objects.filter(category__club__category='2'))
        serializers = ClubSerializer(queryset, many=True)
        return Response(serializers.data)

# 봉사
@api_view(['GET'])
def list_voluteer(request):
    if request.method == 'GET':
        queryset = set(Club.objects.filter(category__club__category='3'))
        serializers = ClubSerializer(queryset, many=True)
        return Response(serializers.data)

# 종교
@api_view(['GET'])
def list_religion(request):
    if request.method == 'GET':
        queryset = set(Club.objects.filter(category__club__category='4'))
        serializers = ClubSerializer(queryset, many=True)
        return Response(serializers.data)

# 운동
@api_view(['GET'])
def list_athletic(request):
    if request.method == 'GET':
        queryset = set(Club.objects.filter(category__club__category='5'))
        serializers = ClubSerializer(queryset, many=True)
        return Response(serializers.data)

# 학술
@api_view(['GET'])
def list_academic(request):
    if request.method == 'GET':
        queryset = set(Club.objects.filter(category__club__category='6'))
        serializers = ClubSerializer(queryset, many=True)
        return Response(serializers.data)

# 동아리 등록
@api_view(['POST'])
def register_club(request):
    if request.method == 'POST':
        serializer = ClubSerializer(data=request.data)
        response = Response()
        if not serializer.is_valid():
            response.data = {'result': 'Fail'}
            return response
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response.data = serializer.data
        return response


# @api_view(['POST'])
# def is_interested(request):
#     if request.method == 'POST':
#         dict_req = dict(json.loads(request.body))
#         print(dict_req)
#         # print(dict_req['username'])
#         # print(dict_req['club_name'])
#         # try:
#         username = dict_req['username']
#         # except TypeError:
#         #     print("username")
#
#         # try:
#         club_name = dict_req['club_name']
#         # except TypeError:
#         #     print("club_name")
#         club_obj = Club.objects.get(name=club_name)
#         if club_obj.interested.filter(username=username):
#             return Response(data={'interested': 'True'})
#         else:
#             return Response(data={'interested': 'False'})


@api_view(['POST'])
def add_interested(request):
    if request.method == 'POST':
        username = json.loads(request.body)['username']
        club_name = json.loads(request.body)['club_name']
        club_obj = Club.objects.get(name=club_name)
        club_obj.interested.add(User.objects.filter(username=username).first())
        # interesting_club = User.objects.filter(username=username).first().interesting
        # interesting_club.add(club_name)
        return Response(data={'result': 'added'})


@api_view(['POST'])
def del_interested(request):
    if request.method == 'POST':
        username = json.loads(request.body)['username']
        club_name = json.loads(request.body)['club_name']
        club_obj = Club.objects.get(name=club_name)
        club_obj.interested.remove(User.objects.filter(username=username).first())
        return Response(data={'result': 'deleted'})