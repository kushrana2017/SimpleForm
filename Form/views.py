# Create your views here.
import datetime

from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Account
from .models import LogInInfo
from .models import Admin

register = template.Library()

# This variable is for storing the username entered when a user logs-in
uname = ''
u_type = ''
alert = ''


# This module handles the logging of activities by saving logs to a plaintext file which is then rendered
# in HTML for administrators to view.

# This module handles the generic template view for the index page in which users will log-in or register
# if they have not made credentials.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'user_login_information'

    def get_queryset(self):
        return LogInInfo.objects.order_by('-username')


# This module simply renders the HTML page for the registration screen.
def registerP(request):
    return render(request, 'registerP.html')


# This module handles the user registration. The "LogInInfo" object is used to store their credentials in the database.
def createPLogIn(request):
    firstName = (request.POST['firstName'])
    lastName = (request.POST['lastName'])
    paddress = (request.POST['address'])
    number = (request.POST['number'])
    email = (request.POST['email'])
    username = (request.POST['username'])
    password = (request.POST['password'])

    try:
        logininfo = LogInInfo.objects.get(username=username)
    except ObjectDoesNotExist:
        LogInInfo.objects.create(username=username, password=password)
        global uname
        uname = username

        Account.objects.create(username=username, firstName=firstName, lastName=lastName, paddress=paddress,
                               number=number, email=email)

        return HttpResponseRedirect(reverse('SimpleForm:index', args=()))
    else:
        return render(request, 'registerP.html', {
            'username': username,
            'error_message': "Username already exists.",
        })


# This module simply renders the HTML page for the password change screen.
# This module handles the attempt of a user to log-in to their profile. If the username and password are valid,
# the user is redirected to their profile. If not, an error message is generated and the user is
# redirected to the index page.
def verify(request):
    username = (request.POST['username'])
    passwordInput = (request.POST['password'])
    utype = (request.POST['type'])
    global u_type
    u_type = utype
    print(u_type)
    try:
        current = LogInInfo.objects.get(username=username)
    except LogInInfo.DoesNotExist:
        return render(request, 'index.html', {
            'username': username,
            'error_message': "There was a problem with your username.",
        })
    else:
        passwordActual = current.password
        if passwordInput == passwordActual:
            global uname
            uname = username
            return HttpResponseRedirect(reverse('SimpleForm:home', args=()))
        else:
            return render(request, 'index.html', {
                'username': username,
                'error_message': "There was a problem with your password.",
            })


# This module simply renders the home page for a user
def home(request):
    print(u_type)
    try:
        at = Admin.objects.get(username=uname)
    except Admin.DoesNotExist:
        try:
            at = Account.objects.get(username=uname)
        except Account.DoesNotExist:
            return HttpResponseRedirect(reverse('SimpleForm:logOut', args=()))
        else:
            utype = "Account"
    else:
        utype = "Admin"

    print(u_type)
    if u_type == "Admin":
        users = Account.objects.all()
        utype = "Admin"
        context = {'user': at,
                   'users': users,
                   'type': utype}
        return render(request, 'home.html', context)
    else:
        return HttpResponseRedirect(reverse('SimpleForm:logOut', args=()))


# This module handles logging-out a user. Afterwards the user is redirected to the index screen.
def logOut(request):
    global uname
    return HttpResponseRedirect(reverse('SimpleForm:index', args=()))
