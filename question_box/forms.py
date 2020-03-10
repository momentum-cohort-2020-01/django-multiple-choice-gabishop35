from django import forms
from question_box.models import Question, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'body', 'creator')


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('response', )