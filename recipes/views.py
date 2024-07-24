from django.shortcuts import render
from django.http import HttpResponse 
from .models import *
from .serializers import * 

def index(request): 
    queryset = models.Recipe.objects.all()
    serializer_class = RecipeSerializer
    return HttpResponse("hello world")
# Create your views here.
