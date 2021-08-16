from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from datetime import datetime, date, time, timedelta
from django.db.models import Sum
import calendar
import bcrypt

def index(request):
    return render(request, 'index.html')

def login_form(request):
    return render(request, 'login.html')

def login_query(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
    print(request.POST['email'])
    userRecord = User.objects.get(email = request.POST['email'])
    request.session['session_id'] = userRecord.id
    return redirect('/dashboard')

def register_form(request):
    return render(request, 'register.html')

def register_record(request):
    if request.method == 'POST':
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/register_form')
        else:
            passwordBcrypt = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            userRecord = User.objects.create(first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            level = 2,
            status = 1,
            password = passwordBcrypt.decode())
            request.session['session_id'] = userRecord.id
    return redirect('/')

def dashboard(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id'])
    }
    return render(request, 'dashboard.html', context)

def close(request):
    request.session.clear()
    return redirect('/')


def view(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_users": User.objects.filter(status=1).order_by("last_name","first_name")
    }
    return render(request, 'view.html', context)

def delete(request,number):
    if 'session_id' not in request.session:
        return redirect('/')
    this_user=User.objects.get(id=number)
    this_user.status = 2
    this_user.save()
    return redirect('/view')

def edit(request,number):
    if 'session_id' not in request.session:
        return redirect('/edit')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_user": User.objects.get(id=number)
    }  
    return render(request,"edit.html",context)


def update(request):
    if request.method == 'POST':
        errors = User.objects.user_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['user_id']+'/edit')
        else:
            passwordBcrypt = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            this_user = User.objects.get(id = request.POST['user_id'])
            this_user.first_name  = request.POST['first_name']
            this_user.last_name = request.POST['last_name']
            this_user.email = request.POST['email']
            this_user.phone = request.POST['phone']
            this_user.password = passwordBcrypt.decode()
            this_user.level = request.POST['level']
            this_user.save()
    return redirect('/view')
