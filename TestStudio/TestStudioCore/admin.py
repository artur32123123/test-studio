from django.contrib import admin
from .models import Questionnaire, Question, QuestionVariant,QuestionnairePass,QuestionnairePassAnswer


admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(QuestionVariant)
admin.site.register(QuestionnairePass)
admin.site.register(QuestionnairePassAnswer)
