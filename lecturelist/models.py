from django.db import models

# Create your models here.
class Lecture(models.Model):
    name = models.EmailField(db_index=True, unique=True)
    summary = models.TextField(max_length=20)
    teacher = models.BooleanField(db_index=True)
    state = models.TextField(max_length=500, blank=True, null=True)
    info = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        pass

    def __str__(self):
        return self.name
