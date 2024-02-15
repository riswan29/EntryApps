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


class Kecamatan(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Kelurahan(models.Model):
    nama = models.CharField(max_length=100)
    kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE)



class EntryData(models.Model):
    NAMA = models.CharField(max_length=100)
    PENDATA = models.CharField(max_length=100)
    NIK = models.CharField(max_length=20)
    TELP = models.CharField(max_length=20)
    TPS = models.CharField(max_length=20)
    KEL = models.CharField(max_length=100)
    KEC = models.CharField(max_length=100)
    KAB = models.CharField(max_length=100)

    
