from django.db import models
from users.models import CustomUser

# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, related_name="recipes")
    category = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=2000)
    equipment = models.CharField(max_length=1000)
    method = models.CharField(max_length=5000)

    def __str__(self):
        return (f"{self.title} from {self.author}")
    
class Batch(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    date = models.DateField(auto_now=False)
    notes = models.CharField(max_length=2000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False, related_name="batches")
    user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, related_name="batches")
    def __str__(self):
        return str(self.recipe.title, self.date)