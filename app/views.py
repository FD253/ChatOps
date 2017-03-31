from rest_framework_mongoengine import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Petition, AMI, User
from .serializers import PetitionSerializer


class PetitionCreate(generics.CreateAPIView):
    serializer_class = PetitionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            pet = Petition.objects.create(**serializer.validated_data)
            import subprocess
            command = 'aws ec2 run run-instances --image-id '
            if request.data['questionnaire'][2]['answer_letter'] == 'a':
                command += 'ami-' + AMI.objects.get(summary='aws-linux').ami + ' '

            if request.data['questionnaire'][2]['answer_letter'] == 'b':
                command += 'ami-' + AMI.objects.get(summary='ubuntu-16.04').ami + ' '

            command += '--count 1 '
            command += '--instance-type ' + 't2.micro '
            command += '--key-name ' + str(User.objects.get(id=request.data['user']).user).lower() + ' '
            command += '--security-groups nginx'
            print(command)

            #-----------TESTING
            command = 'sleep 9; cat /home/fd/Dev/upwork/chatbot_mike/django_backend/app/jsonexample'
            result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            import json
            json_result = json.loads(result.stdout.read().decode('utf-8').replace('\r','').replace('\n',''))
            instance_id = json_result['Instances'][0]['InstanceId']
            print(instance_id)
            #-----------TESTING

            #instance_id = json.loads(result.stdout.read().decode('utf-8').replace('\r', '').replace('\n', ''))['Instances'][0]['InstanceId']
            #get_ip_command = 'sleep 40; aws ec2 describe-instance-status --instance-ids ' + instance_id + '|grep PublicIpAddress| awk \'{print $2}\'| cut -d, -f1| sed \'s/"//g\''
            #result = subprocess.Popen(get_ip_command, stdout=subprocess.PIPE, shell=True)
            #if working then save. but i can't test it so save anyways for now.
            #serializer.save()
            pet.save()
            headers = self.get_success_headers(serializer.data)
            return Response(data={'ip': '123.123.123.123'}, status=status.HTTP_200_OK, headers=headers)


        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)