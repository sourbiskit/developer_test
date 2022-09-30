from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
    path('', views.show_surveys, name='index'),
    path('<int:sur_id>/', views.show_questions, name='show_survey'),
    path('answers/<int:alt_id>/', views.show_answers, name='answers'),
    path('jsonresponse/', views.get_serialized_data, name='get_response')
]
