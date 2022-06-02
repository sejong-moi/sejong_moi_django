from rest_framework import serializers
from .models import Club, Question, Answer

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'introduce', 'introduce_long', 'club_background_url', 'club_logo_url', 'category', 'president_name', 'president_phone_number', 'president', 'questions', 'recruit']


class ClubPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'introduce', 'introduce_long', 'club_background_url', 'club_logo_url', 'president_name', 'president_phone_number', 'recruit', 'apply_link']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['club_name', 'question_text', 'questioner']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question_id', 'answer_text', 'answerer']

