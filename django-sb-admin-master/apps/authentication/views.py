# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from .models import Users, Files
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Account created successfully.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

from django.core.paginator import Paginator

def user_list(request):
    data = Users.objects.filter(isDelete=0)
    context = {'data': data} 
    return render(request, 'accounts/user_list.html',context)

def runAction(request, action, email):
    try:
        user = Users.objects.get(email=email)
        if action == 'Delete':
            if user.isDelete:
                messages.error(request, 'User already deleted')
            else:
                user.isDelete = True
                user.save()
                messages.success(request, 'User successfully deleted')
        elif action == 'Block':
            user.isActive = True
            user.save()
            messages.success(request, 'User successfully blocked')
        elif action == 'Unblock':
            user.isActive = False
            user.save()
            messages.success(request, 'User successfully unblocked')
        else:
            messages.error(request, 'Invalid action')
    except Users.DoesNotExist:
        messages.error(request, 'User not found')
    return redirect('user_list')

def file_list(request):
    file = Files.objects.all()
    context = {'file': file} 
    return render(request, 'accounts/file_list.html',context)

@login_required(login_url="/login/")
def count(request):
    user_count = User.objects.count()
    pdf_count = Files.objects.filter(ext='pdf').count()
    docx_count = Files.objects.filter(ext='docx').count()
    xlsx_count = Files.objects.filter(ext='xlsx').count()
    png_count = Files.objects.filter(ext='png').count()
    jpg_count = Files.objects.filter(ext='jpg').count()

    context = {
        'user_count': user_count,
        'pdf_count': pdf_count,
        'docx_count': docx_count,
        'xlsx_count': xlsx_count,
        'png_count': png_count,
        'jpg_count': jpg_count,
    }
    return JsonResponse(context)


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))




