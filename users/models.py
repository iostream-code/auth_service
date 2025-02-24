from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='student'
    )
    groups = models.ManyToManyField(
        Group, 
        related_name="custom_user_groups", 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, 
        related_name="custom_user_permissions", 
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
