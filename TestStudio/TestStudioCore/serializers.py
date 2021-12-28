from rest_framework import serializers
from .models import Questionnaire, Question, QuestionVariant, QuestionnairePass, QuestionnairePassAnswer, User


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('date_start', None)
        return super().update(instance, validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionVariant
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class QuestionPassAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionnairePassAnswer
        fields = [ 'answer','question' ]


class QuestionnairePassSerializer(serializers.ModelSerializer):
    answers = QuestionPassAnswerSerializer(many=True, read_only=False)

    class Meta:
        model = QuestionnairePass
        fields = '__all__'

    def create(self, validated_data):
        answers = validated_data.pop('answers')
        questionnaire_pass = QuestionnairePass.objects.create(**validated_data)
        for answer in answers:
            QuestionnairePassAnswer.objects.create(questionnaire_pass=questionnaire_pass, **answer)
        return questionnaire_pass
