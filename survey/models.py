from django.db import models


class SurveyQuestionAlternative(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class SurveyQuestion(models.Model):
    alternatives = models.ManyToManyField(SurveyQuestionAlternative, related_name='alternatives')
    text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.text


class Survey(models.Model):
    questions = models.ManyToManyField(SurveyQuestion, related_name='questions')
    title = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField()

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.title


class SurveyUserAnswer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="user")
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, related_name="user")
    alternative = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE, related_name="user")

    name = models.CharField(max_length=50)
    answer_date = models.DateTimeField()

    class Meta:
        ordering = ['answer_date']

    def __str__(self):
        return f"{self.name} - {self.alternative}"
