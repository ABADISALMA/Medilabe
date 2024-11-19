from django.shortcuts import render , redirect
from django.views import View
from .models import Doctor
from .models import Appointment 
from .models import SignUp 
from .forms import AppointmentForm
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#def doctor_list(request):
 #   doctors = doctor.objects.all()  # Utilisez la même casse ici aussi
  #  return render(request, 'doctor.html', {'doctors': doctors})

def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            passwordverif1 = request.POST['password1']
            passwordverif2 = request.POST['password2']
            if passwordverif1 == passwordverif2 :
              form.save()
              username = request.POST['username']
              messages.success(request, "an account was created for " + username )
              return redirect('log')  # Redirection vers la page de connexion après l'inscription
            else:
              messages.error(request,"passwords must be identical ")
              form = SignUpForm()
              return render(request, 'creat.html', {'form': form})
              
    else:
        
        form = SignUpForm()
    return render(request, 'creat.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
       

       email = request.POST.get('email')
       password = request.POST.get('password')

       user = UserCreationForm(request , username=email , password=password)

       if user is not None:
           login(request, user )
           return redirect('hom')
       else:
            messages.error(request, 'Invalid email or password.')
    return render(request,'log.html',{'user':user})
   
def home_view(request):
    return render(request, 'home.html')

@login_required
def dashboard_view(request):
    return render(request, 'base.html')

class Home(View):
    def get(self,request):
        return render(request,'home.html',{})
    
class SUC(View):
    def get(self,request):
        return render(request,'appointment-suc.html',{})
    
class Ser(View):
    def get(self,request):
        return render(request,'services.html',{})
    
class Abo(View):
    def get(self,request):
        return render(request,'about.html',{})

class Hom(View):
    def get(self,request):
        return render(request,'home2.html',{})
    


class Log(View):
    def get(self,request):
        return render(request,'log.html',{})

class Con(View):
    def get(self,request):
        return render(request,'contact.html',{})

class Cre(View):
    def get(self,request):
        return render(request,'creat.html',{})

class  Apo(View):
    def get(self,request):
        return render(request,'appointment.html',{})

class  Dep(View):
    def get(self,request):
        return render(request,'departments.html',{})  

def make_appointment(request): 
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Assurez-vous d'avoir une vue et un template pour la page de succès
    else:
        form = AppointmentForm()
   # return redirect(request, 'creat.html', {'form': form})
    return render(request, 'appointment.html', {'form': form})



def doctor_list(request):
    doctors = Doctor.objects.all()  # Récupérez tous les objets médecin depuis la base de données
    return render(request, 'doctor.html', {'doctors': doctors})

def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'listappo.html', {'appointments': appointments}) 

      

 
