import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Club, Category, Interesting
from login_api.models import User
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

# 관심 동아리 추가
@api_view(['POST'])
def add_interested(request):
    if request.method == 'POST':
        print(json.loads(request.body)) #
        username = json.loads(request.body)['username']
        club_name = json.loads(request.body)['club_name']
        interesting = Interesting.objects.get(username=username)
        club = Club.objects.get(name=club_name)
        interesting.clubs.add(club)
        return Response(data={'result': 'added'})


# 관심 동아리 삭제
@api_view(['POST'])
def del_interested(request):
    if request.method == 'POST':
        print(json.loads(request.body)) #
        username = json.loads(request.body)['username']
        club_name = json.loads(request.body)['club_name']
        interesting = Interesting.objects.get(username=username)
        club = Club.objects.get(name=club_name)
        interesting.clubs.remove(club)
        return Response(data={'result': 'deleted'})