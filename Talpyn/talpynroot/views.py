from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'talpynroot/index.html')

def lesson(request):
    return render(request, 'talpynroot/lesson.html')

def temp(request):
    return render(request, 'talpynroot/temp.html')


def authorization(request):
    form            = LoginForm(request.POST or None)
    if form.is_valid():
        username    = form.cleaned_data['username']
        password    = form.cleaned_data['password']
        login_user  = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'talpynroot/authorization.html')


def registration(request):
    try:
        form = RegistrationForm(request.POST or None)

        if form.is_valid():
            form                = RegistrationForm(request.POST or None)
            client_form         = ClientForm(request.POST or None)

            # save into django auth_user table
            new_user            = form.save(commit=False)
            username            = form.cleaned_data['username']
            password            = form.cleaned_data['password']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name  = form.cleaned_data['last_name']
            new_user.email      = form.cleaned_data['email']
            new_user.username   = username
            new_user.set_password(password)
            new_user.save()

            #save into models Client table
            client              = client_form.save(commit=False)
            client.user         = new_user
            client.save()
            login_user          = authenticate(username=username, password=password)

            if login_user:
                login(request,login_user)
                return HttpResponseRedirect(reverse('index'))

        return render(request, 'talpynroot/registration.html', {'form': form})
    except:
        raise Http404('Something maybe you entered the data incorrectly')
        
