from django.db import models


class Survey(models.Model):
    survey_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField()


class SurveyQuestion(models.Model):
    from_survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)


class SurveyQuestionAlternative(models.Model):
    from_question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=200)


class SurveyUserQuestion(models.Model):
    answered = models.ManyToManyField(SurveyQuestionAlternative)
    username = models.CharField(max_length=50)
    answer_date = models.DateTimeField()
