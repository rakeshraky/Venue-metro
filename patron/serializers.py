import rest_framework
from rest_framework import serializers
from . models import FactMembers, Members


class FactMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactMembers
        fields = '__all__'


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'



