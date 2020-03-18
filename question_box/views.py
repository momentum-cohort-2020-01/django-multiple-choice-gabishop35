from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from question_box.models import Question, Answer, Favorite, Category
from users.models import User
from question_box.forms import QuestionForm, AnswerForm
from django.utils.text import slugify
from django.http import JsonResponse
import json
from django.contrib import messages


@login_required
def question_list(request):
    questions = Question.objects.all()
    # favorite_questions = get_user_favorite(request)
    return render(request, 'core/question_list.html', {'questions': questions})

def question_details(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(response=question.pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.response = question
            answer.save()
            return redirect('question-details', pk=pk)
    else:
        form = AnswerForm()
        return render(request, 'core/question_details.html', {'question': question, 'answers':answers, 'form': form, 'user':request.user})

def question_add(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('question-list')
    else:
        form = QuestionForm()
        return render(request, 'core/question_add.html', {'form': form})

# @csrf_exempt
# def question_add(request):
#     data = json.loads(request.body.decode('utf-8'))
#     question_body = data.get("questionBody")
#     question_title = data.get("questionTitle")
#     new_question = Question.objects.create(title=question_title, body=question_body,)
#     if question_body and question_title:
#         return JsonResponse(
#             {
#         "status":"ok",
#         "data": {
#             "pk": new_question.pk,
#             "title": new_question.title,
#             "body": new_question.body,
#         },
#     })


def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if question.creator.pk == request.user.pk:
        question.delete()
        return redirect('question-list')
    else:
        messages.add_message(request, messages.INFO, 'You do not have the authority to delete this question.')


# def answer_add(request, pk):
#     question = get_object_or_404(Question, pk=pk)
#     answers = Answer.objects.filter(response=question.pk)
#     if request.method == "POST":
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.save()
#             return redirect('question-details')
#     else:
#         form = AnswerForm()
#     return render(request, 'core/answer_add.html', {'form': form})


def tagged(request, slug): 
    # Filter books by tag name  
    tag = Category.objects.get(slug=slug)
    questions = Question.objects.filter(tag=tag)
    return render(request, 'core/question_list.html', {'tag': tag, 'questions': questions})


# ********trying to make favorites work************

def favorite(request, question_pk):
    # for favorite in books:
    question = get_object_or_404(Question, pk=question_pk)
    favorite = Favorite.objects.create(owner=request.user, question=question)
    print(favorite)
    return render(request, 'core/question_details.html', {'question': question})

# def get_user_favorite(request):
#     user = User.objects.get(username=request.user.username)
#     favorite_questions = [favorite.questions for favorite in user.favorites.all()]
#     return favorite_questions