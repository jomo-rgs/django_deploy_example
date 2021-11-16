from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    # User is a build in django model we are extending
    # This will have all the fields in the user model user.username
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
