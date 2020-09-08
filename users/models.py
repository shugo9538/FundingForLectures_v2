from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    email = models.EmailField(db_index=True, unique=True)
    password = models.TextField(max_length=20)
    userType = models.BooleanField(db_index=True)
    pr = models.TextField(max_length=500, blank=True, null=True)
    career = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        pass

    def __str__(self):
        return self.email
