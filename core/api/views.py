from rest_framework import viewsets
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    # View for team data
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    # View for person data
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
