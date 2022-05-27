from rest_framework import serializers
from .models import Club, QnA

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'introduce', 'club_logo_url', 'category', 'president_name', 'president_phone_number']


class AskQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = ['question', 'questioner']


class AnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = ['question', 'questioner']


class QnASerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = ['question', 'questioner', 'answer', 'answerer']


