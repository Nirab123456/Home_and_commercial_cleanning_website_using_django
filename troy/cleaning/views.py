from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
import calendar
from calendar import HTMLCalendar
import time
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from PIL import Image
import os
from django.http import FileResponse,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from .models import contact_to_hire


def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact_save(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')  # Use get() with a default value
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        company = request.POST.get('company', '')

        if name == '' or email == '' or phone == '' or subject == '':
            messages.error(request, 'Please fill all the fields')
            return redirect('contact')
        else:
            contact = contact_to_hire(name=name, email=email, phone=phone, subject=subject, message=message, company=company)
            contact.save()
            return redirect('contact')

        