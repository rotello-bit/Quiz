from django.contrib import admin
from quiz.models import *


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Quiz


admin.site.register(Quiz, PostAdmin)
admin.site.register(Question, PostAdmin)
admin.site.register(Option, PostAdmin)
admin.site.register(Answer, PostAdmin)
# Register your models here.
