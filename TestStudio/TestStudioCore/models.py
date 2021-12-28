from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Questionnaire(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()


QUESTION_TYPES = (
    (1, 'Текст'),
    (2, 'Ответ с выбором одного варианта'),
    (3, 'Ответ с выбором нескольких вариантов'),
)


class Question(models.Model):
    text = models.CharField(max_length=60)
    type = models.IntegerField(choices=QUESTION_TYPES)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)


class QuestionVariant(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class QuestionnairePass(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class QuestionnairePassAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionnaire_pass = models.ForeignKey(QuestionnairePass, on_delete=models.CASCADE,related_name='answers',to_field='id')
    answer = models.TextField()
