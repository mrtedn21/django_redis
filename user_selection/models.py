from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    USUAL_USER = 'usual_user'
    MANAGER = 'manager'
    ADMIN = 'admin'

    ROLES_CHOICES = [
        (USUAL_USER, 'Usual user'),
        (MANAGER, 'Manager'),
        (ADMIN, 'Admin'),
    ]

    role_choice = models.CharField(
        max_length=16, choices=ROLES_CHOICES, default=USUAL_USER
    )
    offer = models.BooleanField()
    avatar = models.ImageField()
