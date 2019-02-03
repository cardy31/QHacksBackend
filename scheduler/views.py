from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Scheduler
from scheduler.serializers import SchedulerSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from .getDayEvents import getGapsOfTimeToday


class SchedulerList(generics.ListCreateAPIView):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer


class SchedulerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GoogleHomeEndpoint(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        todos = Scheduler.objects.all()

        res = {
            "fulfillmentText": "You should vacuum today, Hannah!",
            "fulfillmentMessages": [{
                "text": {
                    "text": [
                        "You should vacuum today, Hannah!"
                    ]
                }
            }],
            "source": ""
        }

        return Response(res, status=status.HTTP_200_OK,)


@api_view(['GET'])
def api_root(request, given_format=None):
    return Response({
        'scheduler': reverse('scheduler-list', request=request, format=given_format),
        'user': reverse('user-list', request=request, format=given_format),
    })