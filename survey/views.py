from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    surveys = Survey.objects.order_by('-pub_date')
    context = {
        'surveys': surveys
    }
    return render(request, 'survey/index.html', context)


def show_survey(request, sur_id):
    current_sur = get_object_or_404(Survey, pk=sur_id)
    return render(request, 'survey/show_survey.html', {'current_sur': current_sur})


def show_answers(request, alt_id):
    current_a = get_object_or_404(SurveyQuestionAlternative, pk=alt_id)
    return render(request, 'survey/answers.html', {'current_a': current_a})
