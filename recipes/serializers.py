from rest_framework import serializers
from .models import *

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        mode=Batch
        fields = '__all__'
        
class RecipeSerializer(serializers.ModelSerializer):
    batches = BatchSerializer(many=True)
    class Meta:
        model=Recipe
        fields = ['id', 'title', 'author', 'category', 'ingredients', 'equipment', 'method', 'batches']

