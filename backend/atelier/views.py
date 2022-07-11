
from django.shortcuts import render

from atelier import models

from rest_framework import viewsets
from atelier.serializers import *
from .models import Atelier


class AtelierViews(viewsets.ModelViewSet):
    queryset = Atelier.objects.all()
    serializer_class = AtelierSerializer

class ClientViews(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ConsultantViews(viewsets.ModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer