from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE_CHOICES = (
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
