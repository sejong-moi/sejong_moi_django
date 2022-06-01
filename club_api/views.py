import json
import datetime
from dateutil.parser import parse

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sejong_moi_django import settings
from .form import ImageUploadForm
from .models import Club, Category, Interesting, Question, Answer, LogoImage
from login_api.models import User
from .serializers import ClubSerializer, QuestionSerializer, AnswerSerializer, ClubPostSerializer
from django.core import serializers


# Create your views here.

@api_view(['GET'])
def club(request, name):
    if request.method == 'GET':
        club = Club.objects.get(name=name)
        serializers = ClubSerializer(club)

        response = Response(data=serializers.data)

        question_queryset = []
        for q in serializers.data['questions']:
            question = dict()
            question_object = Question.objects.get(id = q)
            question['id'] = q
            question['club_name'] = question_object.club_name
            question['question_text'] = question_object.question_text
            question['questioner'] = question_object.questioner.id
            # question['answers'] = question_object.answers.id

            answer = dict()
            answer_object = Answer.objects.get(id=question_object.answers.id)
            answer['question_id'] = answer_object.question_id
            answer['answer_text'] = answer_object.answer_text
            answer['answerer'] = answer_object.answerer.id
            question['answers'] = answer

            question_queryset.append(question)

        response.data['questions_list'] = question_queryset

        is_recruiting = '모집 마감'
        if club.recruit == '상시 모집':
            is_recruiting = '모집 중'
        elif club.recruit == '모집 마감':
            is_recruiting = '모집 마감'
        else:
            now = datetime.datetime.now()
            recruit_date = parse(club.recruit)
            recruit_time = datetime.time(23,59,59)
            recruit = datetime.datetime.combine(recruit_date, recruit_time)
            if now <= recruit:
                is_recruiting = '모집 중'

        print(is_recruiting)
        response.data['is_recruiting'] = is_recruiting


        return response


# @api_view(['GET'])
# def list(request):
#     if request.method == 'GET':
#         queryset = Club.objects.all()
#         for q in queryset:
#             q.recruit = '2022/05/01'
#             q.save()
#         serializers = ClubSerializer(queryset, many=True)
#         return Response(serializers.data)

# 랭킹
@api_view(['GET'])
def list_ranking(request):
    if request.method == 'GET':
        category = {1: 'show', 2: 'culture', 3: 'voluteer', 4: 'religion', 5: 'religion', 6: 'athletic', 7: 'academic'}
        queryset = Club.objects.order_by('-like')[:5]
        serializers = ClubSerializer(queryset, many=True)
        response = Response(data=serializers.data)
        for i in range(len(response.data)):
            response.data[i]['category_eng'] = category[response.data[i]['category'][0]]
            response.data[i]['category_kor'] = str(Category.objects.get(id=response.data[i]['category'][0]))
        return response

# 모집중 동아리 리스트
@api_view(['GET'])
def list_recruiting(request):
    if request.method == 'GET':
        recruiting = []
        queryset = Club.objects.all()
        for q in queryset:
            if q.recruit == '상시 모집':
                recruiting.append(q)
                continue
            elif q.recruit == '모집 마감':
                continue
            recruit_date = parse(q.recruit)
            recruit_time = datetime.time(23,59,59)
            recruit = datetime.datetime.combine(recruit_date, recruit_time)
            now = datetime.datetime.now()
            if now <= recruit:
                recruiting.append(q)

            if len(recruiting) >= 5:
                break

        recruiting.sort(key=lambda q: q.recruit)
        serializers = ClubSerializer(recruiting, many=True)
        response = Response(data=serializers.data)
        return response

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
        print(json.loads(request.body)) #
        # print(json.loads(request.body)['category_kor']) #
        # print(json.loads(request.body)['president_id']) #
        serializer = ClubPostSerializer(data=request.data)
        response = Response()
        if not serializer.is_valid():
            print(serializer.data)
            response.data = {'result': 'Fail'}
            return response
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # club = Club.objects.order_by('-id').first()
        club = Club.objects.get(name=json.loads(request.body)['name'])
        club.president = User.objects.get(username=json.loads(request.body)['president_id'])
        category = Category.objects.get(category=json.loads(request.body)['category_kor'])
        club.category.add(category)
        club.save()

        response.data = serializer.data
        return response


# 관심 동아리 추가
@api_view(['POST'])
def add_interested(request):
    if request.method == 'POST':
        username = json.loads(request.body)['username']
        club_name = json.loads(request.body)['club_name']
        interesting = Interesting.objects.get(username=username)
        club = Club.objects.get(name=club_name)
        interesting.clubs.add(club)
        club.like += 1
        club.save()
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
        club.like -= 1
        club.save()
        return Response(data={'result': 'deleted'})


# 질문 등록
@api_view(['POST'])
def ask_question(request):
    if request.method == "POST":
        serializer = QuestionSerializer(data=request.data)
        response = Response()
        if not serializer.is_valid():
            response.data = {'result': 'Fail'}
            return response

        serializer.is_valid(raise_exception=True)
        serializer.save()

        club = Club.objects.get(name = serializer.validated_data['club_name'])
        club.questions.add(Question.objects.order_by('-id').first())

        response.data = {'result': 'Success'}
        return response

# 답변등록
@api_view(['POST'])
def answer_question(request):
    if request.method == "POST":
        serializer = AnswerSerializer(data=request.data)
        response = Response()
        if not serializer.is_valid():
            response.data = {'result': 'Fail'}
            return response
        serializer.is_valid(raise_exception=True)
        serializer.save()

        question_id = serializer.validated_data['question_id']
        print(Question.objects.get(id=int(question_id)))
        question = Question.objects.get(id=int(question_id))
        question.answers = Answer.objects.order_by('-id').first()
        question.save()

        response.data = {'result': 'Success'}
        return response


@api_view(['POST'])
def is_president(request):
    if request.method == "POST":
        print(request.body)
        user_id = json.loads(request.body)['user_id']
        club_name = json.loads(request.body)['club_name']
        club = Club.objects.get(name=club_name)

        if club.president.id == user_id:
            return Response("True")
        else:
            return Response("False")


# 로고 사진 등록
@csrf_exempt
def upload_logo(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            logo_image = LogoImage.objects.create()
            logo_image.picture = form.cleaned_data['image']
            logo_image.save()
            print(logo_image.picture)
            return HttpResponse('http://localhost:8000/media/' + str(logo_image.picture))
    return HttpResponseForbidden('allowed only via POST')

