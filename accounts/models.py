from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


class User(AbstractUser):
    nickname = models.CharField(max_length=10, blank=True)
    picture = ProcessedImageField(
        blank=True,
        upload_to='profile/', 
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 60},
        default='../static/accounts/default_profile.jpg'
    )
    introduce = models.CharField(max_length=100, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')