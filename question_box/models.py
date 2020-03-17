from django.db import models
from users.models import User
from django.utils.text import slugify


class Question(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="questions")
    tag = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"Question title {self.title}, body {self.body}, created_at {self.created_at}, creator {self.creator}"

class Answer(models.Model):
    response_body = models.TextField()
    response = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    response_date = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"Answer response_body{self.response_body}, response {self.response}, response_date {self.response_date}"

class Category(models.Model):
    name = models.CharField(max_length = 40)
 #trying to add slug
    slug = models.SlugField(null=False, unique=True, default=slugify(name))
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Favorite(models.Model):
    owner = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, related_name='favorites', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Favorite: {self.owner},  Question: {self.question}"

class Correct(models.Model):
    pass