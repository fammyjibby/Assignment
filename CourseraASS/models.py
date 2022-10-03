from django.db import models

# Create your models here.
class Question(models.Model):
    questions = models.CharField(max_length=100)

    def __str__(self):
        return self.questions


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer
