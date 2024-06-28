from rest_framework import serializers
from .models import Team, Person


class PersonSerializer(serializers.ModelSerializer):
    # Serialization of person data
    class Meta:
        model = Person
        fields = ['id', 'name', 'surname', 'email', 'team']


class TeamSerializer(serializers.ModelSerializer):
    # Serialization of team data
    people = PersonSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'people']
