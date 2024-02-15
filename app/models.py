from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('entry', 'Entry'),
        ('perbaikan', 'Perbaikan'),
        ('keuangan', 'Keuangan'),
        ('dapal', 'Dapal'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)