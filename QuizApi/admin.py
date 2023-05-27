from django.contrib import admin
from .models import Quiz, QuizQuestions

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['name','start_time','end_time']

@admin.register(QuizQuestions)
class QuizQuestionsAdmin(admin.ModelAdmin):
    list_display = ['quiz','question','options','answer']
