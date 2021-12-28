from django.utils.datetime_safe import date
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import QuestionnaireSerializer, QuestionSerializer, QuestionVariantSerializer, \
    QuestionnairePassSerializer
from .models import Questionnaire, Question, QuestionnairePass


class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    @action(methods=[ 'get' ], detail=False, url_path="active")
    def get_active(self, request):
        try:
            questionnaire = Questionnaire.objects.filter(date_start__lte=date.today(), date_end__gte=date.today())
            serializer_context = {
                'request': request,
            }
            serializer = QuestionnaireSerializer(questionnaire, many=True, context=serializer_context)
            return Response(serializer.data)
        except Questionnaire.DoesNotExist:
            from rest_framework import status
            return Response(status=status.HTTP_404_NOT_FOUND)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionVariantViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionVariantSerializer


class QuestionnairePassViewSet(CreateModelMixin,
                               ListModelMixin,
                               viewsets.GenericViewSet):
    queryset = QuestionnairePass.objects.all()
    serializer_class = QuestionnairePassSerializer
    filter_backends = [ DjangoFilterBackend ]
    filterset_fields = ['user']
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.auth == None:
            request.user = None
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases
    #     for the currently authenticated user.
    #     """
    #     user_id = self.kwargs[ 'user' ]
    #     return QuestionnairePass.objects.filter(user=user_id)
    #
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)