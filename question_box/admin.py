from django.contrib import admin
from question_box.models import Question, Answer, Favorite, Category
# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Favorite)
admin.site.register(Category)
