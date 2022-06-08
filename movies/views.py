from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata


# Create your views here.

class MovieViewset(viewsets.ModelViewSet):
    
    queryset = Moviedata.objects.all()
    
    serializer_class = MovieSerializer


class ActionViewset(viewsets.ModelViewSet):
    
    queryset = Moviedata.objects.filter(movietype='action')
    serializer_class = MovieSerializer
    
    
    
class CommedyViewset(viewsets.ModelViewSet):
    
    queryset = Moviedata.objects.filter(movietype='commedy')
    serializer_class = MovieSerializer    
    