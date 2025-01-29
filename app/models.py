# Create your models here.
# class TodoItem(models.Model):
#     title=models.CharField(max_length=200)
#     completed=models.BooleanField(default=False)

# class CustomUser(AbstractUser):
#     email=models.EmailField(unique=True)
#     REQUIRED_FIELDS=['email']


#     def __str__(self):
#         return self.username # returns username only
from django.contrib.auth.models import AbstractUser
from django.db import models

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'  # Use email as the username for authentication
    REQUIRED_FIELDS = ['username']  # Optional, set the required fields for create superuser

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
