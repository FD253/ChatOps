from rest_framework_mongoengine import serializers
from .models import Questionnaire, Petition


class QuestionnaireSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class PetitionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Petition
        fields = '__all__'
