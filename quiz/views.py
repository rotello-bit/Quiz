from django.shortcuts import render
from quiz.models import *


def home(request, pk):

    context = {
        'questions': QuestionModel.objects.filter(id=pk),
    }

    return render(request, 'quiz.html', context)



