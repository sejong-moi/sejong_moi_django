
from django.db import models
from login_api.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class Club(models.Model):
    name = models.CharField(max_length=20, unique=True)
    introduce = models.TextField()
    introduce_long = models.TextField()
    club_logo_url = models.URLField()
    category = models.ManyToManyField(Category)
    president_name = models.CharField(max_length=20)
    president_phone_number = models.CharField(max_length=20)
    member = models.ManyToManyField(User, related_name='member')
    interested = models.ManyToManyField(User, related_name='interested')

    def __str__(self):
        return self.name


class Interesting(models.Model):    # 학번 -> 관심 동아리 목록들
    username = models.CharField(max_length=20)
    clubs = models.ManyToManyField(Club)

    def __str__(self):
        return self.username

class Club_Img(models.Model):
	title = models.CharField(max_length=50)
	photo = models.ImageField(blank=True,upload_to="club_logo")