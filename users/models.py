from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class CustomUserManager(UserManager):
    def create_user(self, email, password, userType, pr, career):
        user = self.model(
            email = email,
            password = password,
            userType = userType,
            pr = pr,
            career = career,
        )
        user.is_superuser = False
        user.is_admin = False
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    objects = CustomUserManager()

    email = models.EmailField(db_index=True, unique=True, primary_key=True)
    password = models.TextField(max_length=20, null=False)
    user_type = [('student', '수강생'), ('teacher', '강사')]
    userType = models.CharField(db_index=True, choices=user_type, max_length=20)
    pr = models.TextField(max_length=500, blank=True, null=True)
    career = models.TextField(max_length=500, blank=True, null=True)

    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'email'

    class Meta:
        # permissions = [('student')]
        pass

    def __str__(self):
        return self.email