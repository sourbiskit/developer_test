from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django.http import HttpResponse
import json


def show_surveys(request):
    surveys = Survey.objects.order_by('-pub_date')
    context = {
        'surveys': surveys
    }
    return render(request, 'survey/index.html', context)


def show_questions(request, sur_id):
    current_sur = get_object_or_404(Survey, pk=sur_id)
    return render(request, 'survey/show_survey.html', {'current_sur': current_sur})


def show_answers(request, alt_id):
    current_a = get_object_or_404(SurveyQuestionAlternative, pk=alt_id)
    return render(request, 'survey/answers.html', {'current_a': current_a})


@api_view(['GET'])
def get_serialized_data(request):
    all_surveys = Survey.objects.all()
    all_questions = SurveyQuestion.objects.all()
    all_alternatives = SurveyQuestionAlternative.objects.all()

    survey_ser = SurveySerializer(all_surveys, many=True)
    question_ser = QuestionSerializer(all_questions, many=True)
    alternatives_ser = AlternativesSerializer(all_alternatives, many=True)

    dump = json.dumps({
        'surveys': survey_ser.data,
        'questions': question_ser.data,
        'alternatives': alternatives_ser.data,
    }, ensure_ascii=False).encode('utf8')
    return HttpResponse(dump, content_type='application/json')
