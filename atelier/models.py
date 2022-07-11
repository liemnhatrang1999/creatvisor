from xml.dom.minidom import Document
from django.db import models
from django.views import View



class Atelier(models.Model):
    nomAtelier = models.CharField(max_length=240)
    participant = models.CharField(max_length=240)
    createdDateAtelier = models.DateField(auto_now_add=True)
    majDateAtelier = models.DateField(auto_now=True)
    def __str__(self):
        return self.nomAtelier



class Consultant(models.Model):
    nomConsultant = models.CharField(max_length=240)
    prenomConsultant = models.CharField(max_length=240)
    emailConsultant = models.EmailField()
    mobileConsultant = models.CharField(max_length=20)
    insciptionConsultant = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nomConsultant

class Client(models.Model):
    photo = models.ImageField(null=True,blank =True, upload_to='image')
    nomClient = models.CharField(max_length=240)
    prenomClient = models.CharField(max_length=240)
    emailClient = models.EmailField()
    mobileClient = models.CharField(max_length=20)
    inscriptionClient = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nomClient