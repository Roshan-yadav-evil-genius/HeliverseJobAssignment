from datetime import timedelta
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import QuizSerializer, MCQSolutionSerializer, MCQSerializer, ForClientMCQSerializer
from .models import Quiz, QuizQuestions
from django.utils import timezone
from rest_framework import status


class QuizIntro(ListAPIView):
    def get(self, request):
        return Response({
            "Product": "Quiz APi",
            "For": "Heliverse Job Application",
            "Created By": {
                "name": "Roshan Yadav (FullStack Developer)",
                "email": "roshanyadav1st@gmail.com",
                "phone": "+91-8476868560",
                "Github": "https://github.com/Roshan-yadav-evil-genius",
                "StackOverflow": "https://stackoverflow.com/users/17305921/roshan-yadav"}})


class AddQuiz(CreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class ListQuiz(ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class AddMCQ(APIView):
    def post(self, request, id):
        quiz = Quiz.objects.get(id=id)
        print(request.data)
        request.data["quiz"] = quiz.id
        if isinstance(request.data["options"], list):
            request.data["options"] = ",".join(request.data["options"])
        else:
            return Response({"option": "Please provide options in list format"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = MCQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class ActiveQuiz(APIView):
    def get(self, request):
        current_time = timezone.now()
        print(current_time)
        active_quizzes = Quiz.objects.filter(
            start_time__lte=current_time, end_time__gte=current_time)
        return Response(QuizSerializer(active_quizzes, many=True).data)


class AttemptQuiz(APIView):
    def get(self, request, id):
        quiz = Quiz.objects.get(id=id)
        questions = QuizQuestions.objects.filter(quiz=quiz)
        return Response({"Name": quiz.name, "data": ForClientMCQSerializer(questions, many=True).data})


class QuizSolution(APIView):
    def get(self, request, id):
        quiz = Quiz.objects.get(id=id)
        current_time = timezone.now()

        if current_time >= (quiz.end_time + timedelta(minutes=5)):
            questions = QuizQuestions.objects.filter(quiz=quiz)
            return Response({"Name": quiz.name, "data": MCQSolutionSerializer(questions, many=True).data})
        else:
            time_left = quiz.end_time + timedelta(minutes=5) - current_time
            total_seconds = time_left.total_seconds()
            hours_left = int(total_seconds // 3600)
            minutes_left = int((total_seconds // 60) % 60)
            seconds_left = int(total_seconds % 60)
            time_left_formatted = f"{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}"

            return Response({
                "quize": quiz.name,
                "result": "Not Declared",
                "time left": time_left_formatted})
