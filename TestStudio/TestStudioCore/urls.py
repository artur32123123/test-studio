from .api import QuestionnaireViewSet, QuestionViewSet, QuestionVariantViewSet, QuestionnairePassViewSet
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'api/v1/questionnaires', QuestionnaireViewSet)
router.register(r'api/v1/questions', QuestionViewSet)
router.register(r'api/v1/questions-variants', QuestionVariantViewSet)
router.register(r'api/v1/pass', QuestionnairePassViewSet)
urlpatterns=router.urls