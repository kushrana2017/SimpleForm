from django.urls import re_path
from . import views

app_name = 'SimpleForm'
urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^register/$', views.registerP, name='registerP'),
    re_path(r'^register/create$', views.createPLogIn, name='createPLogIn'),
    re_path(r'^verify/$', views.verify, name='verify'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^logOut/$', views.logOut, name='logOut')
]