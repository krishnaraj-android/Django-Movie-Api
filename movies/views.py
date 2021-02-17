from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(category='action')
    serializer_class = MovieSerializer



class ComedyViewSet(viewsets.ModelViewSet):
  queryset = Moviedata.objects.filter(category='comedy')
  serializer_class = MovieSerializer