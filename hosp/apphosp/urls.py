"""
URL configuration for hosp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index', views.index),
    path('log', views.login),
    path('sign', views.signUp),
    path('signupactn', views.SignUpAction),
    path('logchk', views.loginCheck),
    path('appoint', views.appointmentAction),
    path('home', views.homepg),
    path('logot', views.logout),
    path('adminlg', views.adminlog),
    path('bookdet', views.bookingdet),
    path('admnhome', views.adminHomePage),
    path('adminlogchk', views.adminloginCheck),
    path('adappointpage', views.adappointmentpage),
    path('approveapp/<id>', views.appointment_approve),
    path('rejectapp/<id>', views.appointment_reject),
    path('docform', views.doctorsform),
    path('docaddactn', views.doctorsAction),
    path('docdisp', views.docdisplay),
    path('docdel/<id>', views.doctorDelete)
]
