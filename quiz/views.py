from django.shortcuts import render
from quiz.models import *


def home(request, pk):
    context = {}
    return render(request, 'quiz.html', context)


def get_quizzes(request):
    context = {
        'quizzes': Quiz.objects.all().values('id', 'name')
    }

    return render(request, 'quiz.html', context)


def get_question(request, quiz_id, question_no):
    question = Question.objects.filter(quiz_id=quiz_id, no=question_no).values('id', 'name')
    options = Option.objects.filter(question_id=question.id).valuse('id', 'name')
    context = {
        "question": question,
        "options": options
    }

    return render(request, 'quiz.html', context)
