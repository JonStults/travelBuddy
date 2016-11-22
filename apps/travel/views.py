from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . import models
import bcrypt
import re


def index(request):
    if 'user_id' not in request.session:
        request.session['user_id']= 1
    return render(request, 'travel/index.html')

def login(request):
    username = request.POST.get('username2')
    enteredPW = request.POST.get('password2')

    try:
        user = models.Users.objects.get(username = username)

    except:
        messages.warning(request, 'User does not exist!')
        return redirect('/')
    else:
        if bcrypt.hashpw(enteredPW.encode(), user.password.encode()) == user.password.encode():
            request.session['user_id'] = user.id
            return redirect('/travels')
        else:
            messages.warning(request, 'Password is incorrect!')
            return redirect('/')

def register(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_pw = request.POST.get('confirm_pw')

    if password != confirm_pw:
        messages.warning(request, 'Passwords do not match!')
    else:
        if len(password) < 8:
            messages.warning(request, 'Password needs to be at least 8 characters long!')
        else:
            password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
            result = models.Users.objects.create(name = name, username = username, password = password)
            request.session['user_id'] = result.id
            return redirect('/travels')
    return redirect('/')

def travels(request):
    user = models.Users.objects.get(id = request.session['user_id'])
    details = models.Location.objects.filter(user_id = user)
    joins = models.Join.objects.filter(user_id = user)
    others = models.Location.objects.exclude(user_id = user).exclude(join__in = models.Join.objects.filter(user_id = request.session['user_id']))
    context = {
        'user' : user,
        'details' : details,
        'joins' : joins,
        'others' : others
            }
    return render(request, 'travel/travels.html', context)

def destination(request, id):
    user = request.session['user_id']
    details = models.Location.objects.get(id=id)
    others = models.Join.objects.filter(location_id = details)
    context = {
        'details' : details,
        'others' : others
            }
    return render(request, 'travel/destination.html', context)

def add(request):
    return render(request, 'travel/add.html')

def add_trip(request):
    models.Location.objects.create(user_id = models.Users.objects.get(id = request.session['user_id']), destination = request.POST.get('destination'), description = request.POST.get('description'), start_date = request.POST.get('date_from'), end_date = request.POST.get('date_to'))
    return redirect('/travels')

def join(request, id):
    models.Join.objects.create(user_id = models.Users.objects.get(id = request.session['user_id']), location_id = models.Location.objects.get(id = id))
    return redirect('/travels')

def logout(request):
    del request.session['user_id']
    return redirect('/')




# Create your views here.
