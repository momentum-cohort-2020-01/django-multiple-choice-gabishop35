from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from question_box.models import Question, Answer
from users.models import User
from question_box.forms import QuestionForm
from django.http import JsonResponse
import json

def question_list(request):
    questions = Question.objects.all()
    # answers = Answer.objects.all()
    return render(request, 'core/question_list.html', {'questions': questions})

def question_details(request, pk):
    questions = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.all()
    return render(request, 'core/question_details.html', {'questions': questions, 'answers':answers})

# def question_add(request):
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.save()
#             return redirect('question-list')
#     else:
#         form = QuestionForm()
#         return render(request, 'core/question_add.html', {'form': form})

def question_add(request):
    data = json.loads(request.body.decode('utf-8'))
    return JsonResponse({
        "status":"ok"
    })


def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('question-list')
