"""QRAttendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import TemplateView

from attendance.views import login, generateqr, generateqraction, viewattendanceaction, \
    logout, activateAccount, addQuestion, facultyregistration, \
    studentregistration, getfacultys, getstudents, getquestions, deletefaculty, \
    deletestudent, deletequestion, getfeedback, getquestionfeedback

urlpatterns = [

path('admin/', admin.site.urls),

    path('',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('login/',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('loginaction/',login,name='loginaction'),
    path('activateAccount/',activateAccount,name='activateAccount'),
    path('logout/',logout,name='logout'),

    path('facultyregistration/',TemplateView.as_view(template_name = 'facultyregistration.html'),name='registration'),
    path('facultyregaction/',facultyregistration,name='regaction'),

    path('studentregistration/',TemplateView.as_view(template_name = 'studentregistration.html'),name='registration'),
    path('studentregaction/',studentregistration,name='regaction'),

    path('getstudents/',getstudents,name='regaction'),
    path('getfacultys/',getfacultys,name='regaction'),

    path('deletestudent/',deletestudent,name='regaction'),
    path('deletefaculty/',deletefaculty,name='regaction'),

    path('generateqr/',generateqr,name='registration'),
    path('generateqraction/',generateqraction, name='regaction'),

    path('viewattendance/',TemplateView.as_view(template_name = 'viewattendance.html'),name='regaction'),
    path('viewattendanceaction/',viewattendanceaction, name='regaction'),

    path('addquestion/',TemplateView.as_view(template_name = 'addquestion.html'),name='registration'),
    path('addquestionaction/',addQuestion,name='regaction'),
    path('getquestions/',getquestions,name='regaction'),
    path('deletequestion/',deletequestion,name='regaction'),
    path('getfeedback/',getfeedback,name='regaction'),
    path('getquestionfeedback/',getquestionfeedback,name='regaction'),

]
