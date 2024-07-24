from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    # recipes = models.ForeignKey()
    # so like i dont include batches on the recipe model, and i just bring them in with the serializer
    # here i do the same thing with the users recipes and batches 