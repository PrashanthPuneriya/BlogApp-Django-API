from django.db import models
from django.contrib.auth.models import AbstractUser

from cs_advisory import settings


class MyUser(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    """
    The `USERNAME_FIELD` property tells us which field we will use to log in.
    In Django USERNAME_FIELD is a unique identifier i.e. nickname of the user but not technically 'username'
    """
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    """
    By default in Django USERNAME_FIELD is required field. Now, 'email' is used instead of 'username'.
    So, we now need to include 'username' as required
    """
    REQUIRED_FIELDS = [
        'username', 'first_name']  # If this is empty then we need to create our own Custom Manager class

    def __str__(self):
        return self.email


class MyUserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    github_link = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.email
