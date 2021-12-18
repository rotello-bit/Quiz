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
    question = Question.objects.get(quiz_id=quiz_id, no=question_no)
    options = Option.objects.filter(question_id=question.id).values('id', 'name')
    context = {
        "question": question,
        "options": options
    }

    return render(request, 'quiz.html', context)
