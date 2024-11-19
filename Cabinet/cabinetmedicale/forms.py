from django.core import validators
from django import forms
from .models import Appointment , Doctor , Patient
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import phonenumbers 
from .models import SignUp
import re

class AppointmentForm(forms.ModelForm):
    doctor = forms.ChoiceField(choices=[])

    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'doctor', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].choices = [
            (f"{doctor.nom} {doctor.prenom}", f"{doctor.nom} {doctor.prenom}")
            for doctor in Doctor.objects.all()
        ]

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+212[0-9]{9}$', phone):
            raise forms.ValidationError("Le numéro de téléphone doit être au format +212XXXXXXXXX (9 chiffres après +212).")
        return phone

    def save(self, commit=True):
      appointment = super().save(commit=False)
      if commit:
        appointment.save()
        # Créer un nouvel objet Patient et l'associer à l'objet Appointment
        doctor_name = self.cleaned_data['doctor']
        patient = Patient.objects.create(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data['phone'],
            doctor_name=doctor_name,
            id_appointment=appointment.id
        )
        appointment.patient = patient
        appointment.save()
        return appointment

def is_valid_phone_number(phone_number, country_code):
    try:
        parsed_number = phonenumbers.parse(phone_number, country_code)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

class SignUpForm(forms.ModelForm):
   email = forms.EmailField(required=True)

   class Meta:
       model = SignUp
       fields = ('username', 'email', 'password1', 'password2')
       widgets = {
          'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
             'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
              'password2' : forms.PasswordInput(attrs={'class':'form-control'})
       }
       
   
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'