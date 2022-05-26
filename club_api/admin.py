from django.contrib import admin
from .models import Club, Category, Interesting

# Register your models here.
admin.site.register(Club)
admin.site.register(Category)
admin.site.register(Interesting)