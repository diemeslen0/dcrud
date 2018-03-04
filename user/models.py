from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.generic.models import IBANField
from django.conf import settings


class User(AbstractUser):
    '''
    The user extend AbstractUser and I added 2 new fields
    '''
    iban = IBANField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        '''
        If the user create the account using Google Authentication he will
        no have a creator but in this case will be superuser. If the user
        was created by a superuser, so he will be a normal user.

        If the user is a superuser, the username will be the email. it not,
        we don't need the username.
        '''
        if not self.creator:
            self.is_superuser = True
            self.username = self.email
        else:
            self.is_superuser = False
            self.username = ''
        super().save(*args, **kwargs)

    def __str__(self):
        '''
        Just to not return a object without information
        '''
        return self.first_name

