from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.conf import settings

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=False)
   
    USERNAME_FIELD = 'phone_number'    
    REQUIRED_FIELDS = ['email'] # while creating superuser
    objects = UserManager()

    def __str__(self):
        return self.phone_number
    
class CarsTable(models.Model):
    description_text = models.TextField()
    price = models.IntegerField()
    location = models.CharField(max_length=255)
    model = models.IntegerField()
    kms_ran = models.CharField(max_length=50)
    engine_power = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    image_link = models.TextField()

    class Meta:
        db_table = 'cars'


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(CarsTable, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=False)
    rating = models.IntegerField(null=True, blank=False)