from django import forms
from question_box.models import Question, Answer, Category, Favorite

class QuestionForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Question
        fields = ('title', 'body', 'creator', 'tag')


class AnswerForm(forms.ModelForm):
    response_body = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Answer
        fields = ('response_body',)