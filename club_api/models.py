from django.db import models
from login_api.models import User

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=20)
    introduce = models.TextField()
    club_logo_url = models.URLField()
    president_name = models.CharField(max_length=20)
    president_phone_number = models.CharField(max_length=20)
    member = models.ManyToManyField(User)

    def __str__(self):
        return self.name