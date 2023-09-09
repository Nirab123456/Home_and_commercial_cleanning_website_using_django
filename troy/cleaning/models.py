from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.dispatch import receiver




class contact_to_hire(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000,blank=True,null=True)
    company = models.CharField(max_length=100,blank=True,null=True)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class appointment(models.Model):
    TOPIC_CHOICES = [
        ('commercial', 'commercial'),
        ('resedential', 'resedential'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    appointment_date = models.DateField()
    adress = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, choices=TOPIC_CHOICES)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return self.name
    

    
class Record_mail_me(models.Model):
    TOPIC_CHOICES = [
        ('HIRE_ME', 'HIRE ME'),
        ('CONTACT_ME', 'CONTACT ME'),
        ('COLLABORATION', 'COLLABORATION REQUEST'),
    ]

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(max_length=1000,blank=True,null=True)
    topic = models.CharField(max_length=100, default='CONTACT_ME', choices=TOPIC_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.topic}'

