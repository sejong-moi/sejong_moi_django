from rest_framework import serializers
from .models import Club

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['name', 'introduce', 'club_logo_url', 'category', 'president_name', 'president_phone_number']
