from rest_framework import serializers
from scheduler.models import Scheduler
from django.contrib.auth.models import User

class SchedulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduler
        fields = ('id', 'created', 'name', 'priority', 'lengthOfTime', 'category', 'description', 'user')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'firstname', 'lastname', 'is_staff', 'is_active')
