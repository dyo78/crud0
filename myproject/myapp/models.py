from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    eid = models.IntegerField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    # Remove the username field
    username = None

    # Define the email field as the unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['eid', 'name', 'phone']

    def __str__(self):
        return self.email
