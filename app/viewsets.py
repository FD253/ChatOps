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

    def perform_create(self, serializer):
        import subprocess
        command = 'aws ec2 run run-instances --image-id '
        if self.request.data['questionnaire'][2]['answer_letter'] == 'a':
            command += 'ami-' + AMI.objects.get(summary='aws-linux').ami + ' '

        if self.request.data['questionnaire'][2]['answer_letter'] == 'b':
            command += 'ami-' + AMI.objects.get(summary='ubuntu-16.04').ami + ' '

        command += '--count 1 '
        command += '--instance-type ' + 't2.micro '
        command += '--key-name ' + str(User.objects.get(id=self.request.data['user']).user).lower() + ' '
        command += '--security-groups nginx'
        print(command)
        #p = subprocess.check_output(command)
        #def get_machine_id(p) <- parse to find
        #check_command = 'sleep 30; aws ec2 describe-instance-status --instance-ids i-' + '1234567890abcdef0' #info returned in the subprocess
        #print(check_command)
        #c = subprocess.check_output(check_command)
        #def get_machine_ip(c) <- parse to find
        #if working then save. but i can't test it so save anyways for now.
        serializer.save()


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
