from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for UserProfiles"""

    def create_user(self, email, name, password=None):
        """Create  a new user profile."""
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email) #for making case insensitive for first half of email.
        user = self.model(email=email, name=name)

        user.set_password(password) #password is converted as Hash and saved in database instead of plain text.
        user.save(using=self._db)  #used for saving it to a database.

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details."""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the sysem."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager() #CustomModelManager for the usermodel so it knows how to create users and control users using Django commandline tools.

    USERNAME_FIELD = 'email' #when we create app, instead of USERNAME, we ask for email
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve Full Name of User"""
        return self.name

    def get_short_name(self):
        """Retrieve Short Name of user"""
        return self.name

    def __str__(self): #when you convert a model attribute you need to change everything to string
        """Return String Representation of our user"""
        return self.email
