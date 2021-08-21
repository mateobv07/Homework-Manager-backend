from django.shortcuts import render

# Create your views here.
from .models import Homework 
from .serializers import HomeworkSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class HomeworkViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer