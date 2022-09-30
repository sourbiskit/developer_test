from rest_framework import serializers
from .models import *


class AlternativesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestionAlternative
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    alternatives = SurveyQuestionAlternative.objects.prefetch_related('alternatives')

    class Meta:
        model = SurveyQuestion
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    questions = SurveyQuestion.objects.prefetch_related('questions')

    class Meta:
        model = Survey
        fields = '__all__'
