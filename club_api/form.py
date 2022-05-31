from django import forms

from club_api.models import Category, Question
from login_api.models import User


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


#
# class ClubForm(forms.Form):
#     name = forms.CharField(max_length=20, unique=True)
#     introduce = forms.TextField()
#     introduce_long = forms.TextField()
#     club_logo_url = forms.URLField(default='https://w.namu.la/s/90b3132a0a6406eaf98a49e5d7bf9ef7f7c'
#                                             '689036f892663e4c22de357550b7789a027e7dfb76ccf853857f6ec8'
#                                             'fba152d756ba50388c886d35fb69e0740d22e8509ffa55a7374af9aa'
#                                             '4b32083dd149c53c290ca6b057f8074efcc9895adf6a2')
#     club_background_url = forms.URLField(default='https://w.namu.la/s/90b3132a0a6406eaf98a49e5d7bf9ef7f7c'
#                                             '689036f892663e4c22de357550b7789a027e7dfb76ccf853857f6ec8'
#                                             'fba152d756ba50388c886d35fb69e0740d22e8509ffa55a7374af9aa'
#                                             '4b32083dd149c53c290ca6b057f8074efcc9895adf6a2')
#     category = forms.ManyToManyField(Category)
#     president_name = forms.CharField(max_length=20, blank=True)
#     president_phone_number = forms.CharField(max_length=20, blank=True)
#     member = forms.ManyToManyField(User, related_name='member', blank=True)
#     like = forms.IntegerField()
#     questions = forms.ManyToManyField(Question, related_name='questions', blank=True)
#     president = forms.ForeignKey(User, on_delete=forms.DO_NOTHING, related_name='president', default=1, blank=True)
