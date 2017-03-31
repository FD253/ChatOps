from rest_framework_mongoengine import viewsets
from .serializers import QuestionnaireSerializer, PetitionSerializer,\
    UserSerializer, AMISerializer
from .models import Questionnaire, Petition, User, AMI


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


class AMIViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = AMISerializer

    def get_queryset(self):
        return AMI.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'user'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserViewSetById(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
