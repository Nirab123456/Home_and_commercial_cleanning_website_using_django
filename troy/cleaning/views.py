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


def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')