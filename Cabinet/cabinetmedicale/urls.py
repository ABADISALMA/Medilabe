from . import views
from django.urls import path,include
from .views import signup
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path("",views.Home.as_view(),name='home'),
    path("home2/",views.Hom.as_view(),name='hom'),
    path("log/",views.Log.as_view(),name='log'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home_view, name='home'),  # Assurez-vous d'avoir une vue home_view définie
    path("contact/",views.Con.as_view(),name='con'),
    #path("creat/",views.Cre.as_view(),name='cre'),
    #path("appointment/",views.Apo.as_view(),name='apo'),
    path('login/', views.loginPage, name='login'),
    path('make_appointment/', views.make_appointment, name='apo'),
    #path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('doctors/',views.doctor_list, name='doctor'),
    path('departments/',views.Dep.as_view(), name='dep'),
    path('services/',views.Ser.as_view(), name='ser'),
    path('about/',views.Abo.as_view(), name='abo'),
    path('creat/', views.signup, name='cre'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Page principale après connexion
    path('appointment-suc/', views.SUC.as_view(), name='appointment_success'),
     path('listappo/', views.list_appointments, name='list_appointments'),
]

    