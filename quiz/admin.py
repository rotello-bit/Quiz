from django.contrib import admin
from quiz.models import *


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = QuestionModel


admin.site.register(QuestionModel, PostAdmin)
# Register your models here.
