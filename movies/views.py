from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata
import requests



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



def home(request):
    response_json = requests.get('http://127.0.0.1:8000/api/movies/') 
    if (response_json.status_code == 200):  
        response = response_json.json() 
        print(response)
    # this is the https request for data in json format


# only proceed if I have a 200 response which is saved in status_code

    #converting from json to dictionary using json library
    
    # response = requests.get('https://127.0.0.1:8000/movies/')
  
    # data = response.json()
    # print(data)
    
    
    return render(request,'home/home.html',{'response':response})
    
        