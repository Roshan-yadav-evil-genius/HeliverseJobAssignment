from rest_framework import serializers
from .models import Quiz, QuizQuestions
from django.utils import timezone


class QuizSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = '__all__'

    def get_status(self, obj):
        current_time = timezone.now()
        if obj.start_time <= current_time and obj.end_time >= current_time:
            return "active"
        elif obj.start_time > current_time:
            return "inactive"
        else:
            return "finished"


class MCQSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestions
        fields = '__all__'


class ForClientMCQSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = QuizQuestions
        fields = ["id", "question", "options"]

    def get_options(self, obj):
        return {index+1: value.strip() for index, value in enumerate(obj.options.split(","))}


class MCQSolutionSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()

    class Meta:
        model = QuizQuestions
        fields = ["id", "question", "answer"]

    def get_answer(self, obj):
        mcq = {index+1: value.strip()
               for index, value in enumerate(obj.options.split(","))}
        return mcq[obj.answer]
