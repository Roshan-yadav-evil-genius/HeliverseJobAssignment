from django.urls import path
from .views import QuizIntro,AddQuiz,ListQuiz,QuizSolution,ActiveQuiz,AttemptQuiz,AddMCQ

urlpatterns = [
    path("",QuizIntro.as_view(),name='index'),
    path("quizzes/",AddQuiz.as_view()),
    path("quizzes/all",ListQuiz.as_view()),
    path("quizzes/active",ActiveQuiz.as_view()),
    path("quizzes/<int:id>/result",QuizSolution.as_view()),
    path("quizzes/<int:id>/addQuestion",AddMCQ.as_view()),
    path("quizzes/<int:id>",AttemptQuiz.as_view(),),
]
