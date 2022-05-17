from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Club
from .serializers import ClubSerializer

# Create your views here.

@api_view(['GET'])
def list(request):
    if request.method == 'GET':
        queryset = Club.objects.all()[:8]
        serializers = ClubSerializer(queryset, many=True)
        return Response(serializers.data)