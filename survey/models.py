from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=50, null=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title


class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, related_name='question', on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.text


class SurveyQuestionAlternative(models.Model):
    question = models.ForeignKey(SurveyQuestion, related_name='alternative', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class SurveyUserAnswer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="user")
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, related_name="user")
    alternative = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE, related_name="user")

    name = models.CharField(max_length=50)
    answer_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.alternative}"
