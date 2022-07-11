from rest_framework import serializers
from .models import *

class AtelierSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Atelier
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Client
        fields = '__all__'

class ConsultantSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Consultant
        fields = '__all__'
        