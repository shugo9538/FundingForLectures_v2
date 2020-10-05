from django.db import models
from lecturelist.models import Lecuture

# Create your models here.
class LectureFunding(models.Model):
    funding_title = models.ForeignKey(Lecuture, on_delete=models.CASCADE, related_name='lectures_title', db_column='funding_title')
    funding_summary = models.ForeignKey(Lecuture, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return self.title