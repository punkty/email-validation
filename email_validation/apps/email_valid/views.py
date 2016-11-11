from django.shortcuts import render, redirect
from .models import Email
import re
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
    return render(request, "email_valid/index.html")

def process(request):
    email = request.POST['email']
    print(email)
    if not email:
        messages.error(request, "Email cannot be blank")
        return redirect("/")
    elif not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request, "Must be a valid email")
        return redirect("/")

    request.session['email'] = email
    Email.objects.create(email=email)

    return redirect('/success')

def success(request):
    if "email" not in request.session:
        return redirect("/")
    context = {
        'emails': Email.objects.all(),
    }
    return render(request, "email_valid/success.html", context)

def clear(request):
    request.session.clear()
    return redirect('/')
