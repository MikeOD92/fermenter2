from django.shortcuts import render
from django.http import HttpResponse 
from recipes.models import Recipe
from .serializers import * 

def index(request): 
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    return HttpResponse("hello world")
# Create your views here.
