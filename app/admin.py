from django.contrib import admin
from .models import questions,Comment
# Register your models here.

admin.site.register(questions)
admin.site.register(Comment)