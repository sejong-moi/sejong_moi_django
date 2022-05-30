from django.contrib import admin
from .models import Club, Category, Interesting, Answer, Question, LogoImage

# Register your models here.
admin.site.register(Club)
admin.site.register(Category)
admin.site.register(Interesting)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(LogoImage)