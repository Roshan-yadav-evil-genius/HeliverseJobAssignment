from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=100,unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"Quiz : {self.id} Name : {self.name}"

class QuizQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    options = models.CharField(max_length=1000)
    answer = models.IntegerField()