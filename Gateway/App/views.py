from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from guruskull_utils.models import UserMaster
# Create your views here.

class Welcome(APIView):
    def get(self, request):
        return Response({'message': 'Hello, world!'})