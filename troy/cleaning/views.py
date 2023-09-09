from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.http import FileResponse,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import contact_to_hire, Record_mail_me , SUBSCRIPTION
from .models import appointment as APPOINMENT

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

    else:
        return redirect('contact')
    
def appointment(request):
    return render(request,'appointment.html')

def appointment_save(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        print(name)
        email = request.POST.get('email', '')
        print(email)
        phone = request.POST.get('phone', '')
        print(phone)
        appointment_date = request.POST.get('appoinment_date', '')
        print(appointment_date)
        adress = request.POST.get('address', '')
        print(adress)
        topic = request.POST.get('topic', '')
        print(topic)

        if name == '' or email == '' or phone == '' or appointment_date == '' or adress == '' or topic == '':
            messages.error(request, 'Please fill all the fields')
            return redirect('appointment')
        else:
            appointment = APPOINMENT(name=name, email=email, phone=phone, appointment_date=appointment_date, adress=adress, topic=topic)
            appointment.save()
            return redirect('appointment')
        
    else:
        return redirect('appointment')
    

def developer(request):
    return render(request,'about_developer.html')

def developer_save(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')  # Use get() with a default value
        topic = request.POST.get('topic', '')
        message = request.POST.get('message', '')
        if name == '' or email == '' or phone == '' or topic == '':
            messages.error(request, 'Please fill all the fields')
            return redirect('developer')
        else:
            contact = Record_mail_me(name=name, email=email, phone=phone, topic=topic, message=message)
            contact.save()
            return redirect('developer')

    else:
        return redirect('developer')
    

def subscription(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        if email == '':
            messages.error(request, 'Please fill all the fields')
            return redirect('home')
        else:
            contact = SUBSCRIPTION(email=email)
            contact.save()
            return redirect('home')

    else:
        return redirect('home')