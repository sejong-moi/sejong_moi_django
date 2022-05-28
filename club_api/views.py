import json

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .form import ImageUploadForm
from .models import Club, Category, Interesting, Question, Answer, ExampleModel
from login_api.models import User
from .serializers import ClubSerializer, QuestionSerializer, AnswerSerializer
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
        return response


# @api_view(['GET'])
# def list(request):
#     if request.method == 'GET':
#         queryset = Club.objects.all()
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
        user = request.body['user']
        president = request.body['president']
        if user == president:
            return Response("True")
        else:
            return Response("False")



# 사진 등록
# https://kgu0724.tistory.com/117
@csrf_exempt
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.create()
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')



