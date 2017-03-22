from rest_framework_mongoengine import viewsets
from .serializers import QuestionnaireSerializer, PetitionSerializer
from .models import Questionnaire, Petition


class QuestionnaireViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = QuestionnaireSerializer

    def get_queryset(self):
        return Questionnaire.objects.all()


class PetitionViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PetitionSerializer

    def get_queryset(self):
        return Petition.objects.all()
