from django.contrib import admin
from .models import Doctor
from .models import Appointment 
from .models import Patient

#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.models import User
from .models import SignUp

#class CustomUserAdmin(BaseUserAdmin):
 #   add_form = SignUpForm
  #  add_fieldsets = (
   #     (None, {
    #        'classes': ('wide',),
     #      'fields': ('username', 'email', 'password1', 'password2'),
      #  }),
    #)

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)

@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password1', 'password2')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'doctor', 'message')
  

#admin.site.unregister(User)
#admin.site.register(User, CustomUserAdmin)