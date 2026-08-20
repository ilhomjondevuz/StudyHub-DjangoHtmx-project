from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import BaseModel


ADMIN, TEACHER, ORDINARY = 'admin', 'teacher', 'ordinary'
ROLE_CHOICES = (
    (ADMIN, 'Admin'),
    (TEACHER, 'Teacher'),
    (ORDINARY, 'Ordinary'),
)

class User(AbstractUser, BaseModel):
    role = models.CharField(max_length=8, choices=ROLE_CHOICES, default=ORDINARY)
    avatar = models.ImageField(upload_to='avatars/%Y/%m', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User '
        verbose_name_plural = 'Users'
        ordering = ('username',)