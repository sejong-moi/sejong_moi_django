from bs4 import BeautifulSoup
from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Club, Category
from .serializers import ClubSerializer

# Create your views here.

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
        queryset = set(Club.objects.filter(category__club__category='6'))
        serializers = ClubSerializer(queryset, many=True)
        return Response(serializers.data)
