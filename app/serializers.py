from rest_framework_mongoengine import serializers
from .models import Questionnaire, Petition, User, AMI


class QuestionnaireSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class PetitionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Petition
        fields = '__all__'


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = ["user", "charge_code", "id"]


class AMISerializer(serializers.DocumentSerializer):
    class Meta:
        model = AMI
        fields = '__all__'
