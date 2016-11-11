from django.shortcuts import render, redirect
from .models import Email
import re
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
    return render(request, "email_valid/index.html")

def process(request):
    email = request.POST  
    if not email:
        message.add_message(request, messages.INFO, "Email cannot be blank")
        return redirect("/")

    Email.objects.create(email=email)
    return render(request, "email_valid/success.html")

def success(request):

    return render(request, "email_valid/success.html", context)
        