from django import forms

from club_api.models import Category, Question
from login_api.models import User


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

