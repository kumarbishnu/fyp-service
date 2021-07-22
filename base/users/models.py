from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='user_profiles')

    def __str__(self):
        return self.user.first_name
