from django.db import models
from users.models import User

# Create your models here.
class Lecuture(models.Model):
    lecture_title = models.CharField(db_index=True, max_length=20, null=False)
    lecture_summary = models.TextField(max_length=100, null=False)
    # lecture_user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture_detail = models.TextField(max_length=500, null=True)

    class Meta:
        pass

    def __str__(self):
        return self.lecture_title