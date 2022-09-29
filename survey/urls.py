from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sur_id>/', views.show_survey, name='show_survey'),
    path('answers/<int:alt_id>/', views.show_answers, name='answers')
]
