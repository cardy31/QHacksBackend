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
from .insertIntoCalendar import insertIntoCal


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
        gaps = getGapsOfTimeToday()
        todos = Scheduler.objects.all()
        if gaps is None:
            res = {
                "fulfillmentText": todos[0].Name,
                "fulfillmentMessages": [{
                    "text": {
                        "text": [
                            "You should vacuum today, Hannah!"
                        ]
                    }
                }],
                "source": ""
            }
            return Response(res, status=status.HTTP_200_OK, )
        for todo in todos:
            for time,length in gaps:
                if todo.lengthOfTime <= length:
                    res = {
                        "fulfillmentText": todo.name,
                        "fulfillmentMessages": [{
                            "text": {
                                "text": [
                                    "You should " + todo.name + " today, Hannah!"
                                ]
                            }
                        }],
                        "source": ""
                    }
                    insertIntoCal(todo.name, time, length)
                    return Response(res, status=status.HTTP_200_OK, )


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