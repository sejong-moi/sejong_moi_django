
from django.db import models
from login_api.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


# class QnA(models.Model):
#     club_name = models.CharField(max_length=20)
#     question = models.TextField()
#     questioner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questioner1')
#     answer = models.TextField(blank=True)
#     answerer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answerer1', blank=True)
#
#     def __str__(self):
#         return str(self.id)


class Answer(models.Model):
    question_id = models.IntegerField(default=0) # 0 이면 빈 답변 이라는 뜻
    answer_text = models.TextField(default='아직 답변이 없습니다.')
    answerer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answerer', default='admin')

    def __str__(self):
        return str(self.id)


class Question(models.Model):
    club_name = models.CharField(max_length=20, blank=True)
    question_text = models.TextField()
    questioner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questioner')
    answers = models.ForeignKey(Answer, on_delete=models.CASCADE, default='18', related_name='answers')
    # 18번 질문이 기본 답변 (더미노드)

    def __str__(self):
        return str(self.id)



class Club(models.Model):
    name = models.CharField(max_length=20, unique=True)
    introduce = models.TextField()
    introduce_long = models.TextField()
    club_logo_url = models.URLField(default='https://w.namu.la/s/90b3132a0a6406eaf98a49e5d7bf9ef7f7c'
                                            '689036f892663e4c22de357550b7789a027e7dfb76ccf853857f6ec8'
                                            'fba152d756ba50388c886d35fb69e0740d22e8509ffa55a7374af9aa'
                                            '4b32083dd149c53c290ca6b057f8074efcc9895adf6a2')
    club_background_url = models.URLField(default='https://w.namu.la/s/90b3132a0a6406eaf98a49e5d7bf9ef7f7c'
                                            '689036f892663e4c22de357550b7789a027e7dfb76ccf853857f6ec8'
                                            'fba152d756ba50388c886d35fb69e0740d22e8509ffa55a7374af9aa'
                                            '4b32083dd149c53c290ca6b057f8074efcc9895adf6a2')
    category = models.ManyToManyField(Category)
    president_name = models.CharField(max_length=20, blank=True)
    president_phone_number = models.CharField(max_length=20, blank=True)
    member = models.ManyToManyField(User, related_name='member', blank=True)
    like = models.IntegerField()
    questions = models.ManyToManyField(Question, related_name='questions', blank=True)
    president = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='president', default=1, blank=True)

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