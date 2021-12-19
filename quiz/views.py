from django.shortcuts import render
from quiz.models import *
from django.http import JsonResponse, HttpResponse
from django.template import loader
import json


def home(request):
    return render(request, 'main.html', {})


def get_quizzes(request):
    t = loader.get_template('quiz.html')
    c = {
        'quizzes': Quiz.objects.all().values('id', 'name')
    }
    return HttpResponse(t.render(c, request), content_type='text/html')


def get_question(request, quiz_id, question_no):
    question = Question.objects.filter(quiz_id=quiz_id, no=question_no).order_by('no').values('id', 'name', 'quiz_id', 'no')
    options = Option.objects.filter(question_id=question[0]["id"]).values('id', 'name', 'no')
    first = Question.objects.all().order_by('no').first()
    last = Question.objects.all().order_by('no').last()

    t = loader.get_template('question.html')
    c = {
        "question": question[0],
        "options": options,
        "is_first": first.no == question_no,
        "is_last": last.no == question_no,
        "quiz_id": quiz_id
    }

    return HttpResponse(t.render(c, request), content_type='text/html')


def submit_quiz(request):
    result = json.loads(request.POST["result"])
    quiz_id = request.POST["quiz_id"]
    answers = Answer.objects.filter(question__quiz_id=quiz_id).values('question__id', 'question__no', 'option_id')

    question_count = len(answers)
    correct_answer_count = 0
    for answer in answers:
        if answer["option_id"] == int(result["question_" + str(answer["question__no"])]):
            correct_answer_count += 1

    t = loader.get_template('result.html')
    c = {
        'question_count': question_count,
        "correct_answer_count": correct_answer_count,
        "wrong_answer_count": question_count - correct_answer_count,
        "success_rate": int(100*correct_answer_count/question_count)
    }
    return HttpResponse(t.render(c, request), content_type='text/html')
