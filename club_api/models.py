
from django.db import models
from login_api.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class QnA(models.Model):
    club_name = models.CharField(max_length=20)
    question = models.TextField()
    questioner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questioner')
    answer = models.TextField(blank=True)
    answerer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answerer', blank=True)

    def __str__(self):
        return str(self.id)

class Club(models.Model):
    name = models.CharField(max_length=20, unique=True)
    introduce = models.TextField()
    introduce_long = models.TextField()
    club_logo_url = models.URLField()
    category = models.ManyToManyField(Category)
    president_name = models.CharField(max_length=20, blank=True)
    president_phone_number = models.CharField(max_length=20, blank=True)
    member = models.ManyToManyField(User, related_name='member', blank=True)
    # interested = models.ManyToManyField(User, related_name='qna')
    like = models.IntegerField()
    qna = models.ManyToManyField(QnA, related_name='qna', blank=True)

    def __str__(self):
        return self.name


class Interesting(models.Model):    # 학번 -> 관심 동아리 목록들
    username = models.CharField(max_length=20)
    clubs = models.ManyToManyField(Club, blank=True)

    def __str__(self):
        return self.username

class Club_Img(models.Model):
	title = models.CharField(max_length=50)
	photo = models.ImageField(blank=True,upload_to="club_logo")