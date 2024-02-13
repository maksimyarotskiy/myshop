from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    cart = models.OneToOneField('store.Cart', null=True, blank=True, on_delete=models.SET_NULL, related_name='user_profile')

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return f'user address: {self.address}'
