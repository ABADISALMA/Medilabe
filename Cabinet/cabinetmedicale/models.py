from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.
class Doctor(models.Model):
    matricule = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    spec = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    doctor = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"Appointment for {self.name} with {self.doctor} on {self.date}"
    
    def clean(self):
        # Validate phone number format for Morocco
        if not re.match(r'^\+212[0-9]{9}$', self.phone):
            raise ValidationError('Phone number must be in the format +212XXXXXXXXX (9 digits after +212)')
        
class SignUp(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    id_appointment = models.IntegerField(null=True, blank=True)
    

    def __str__(self):
        return self.name





    


