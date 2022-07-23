from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USUAL_USER = 'usual_user'
    MANAGER = 'manager'
    ADMIN = 'admin'

    ROLES_CHOICES = [
        (USUAL_USER, 'Usual user'),
        (MANAGER, 'Manager'),
        (ADMIN, 'Admin'),
    ]

    role_choice = models.CharField(
        max_length=16, choices=ROLES_CHOICES, default=USUAL_USER, null=True
    )
    offer = models.BooleanField(null=True)
    avatar = models.ImageField(null=True)
