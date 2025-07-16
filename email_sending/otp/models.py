from django.db import models
from django.contrib.auth.models import AbstractUser
from otp.manager import UserManager
# Create your models here.
class CustomUser(AbstractUser):
    username = None

    phone_number = models.CharField(max_length=12,unique=True)
    profile = models.ImageField(upload_to='profile/' , null=True , blank=True)
    is_verified = models.BooleanField(null=True , blank= True)
    otp = models.IntegerField(default=0)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'
    

    objects = UserManager()