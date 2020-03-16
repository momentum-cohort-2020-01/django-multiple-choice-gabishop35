from django import forms
from question_box.models import Question, Answer

class QuestionForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Question
        fields = ('title', 'body', 'creator')


class AnswerForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Answer
        fields = ('response_body',)