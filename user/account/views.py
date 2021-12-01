import random
import requests
from django.shortcuts import render
from .models import Register
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def register(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Email = request.POST['email']
        Mobile_number = request.POST['mobile']
        Password = request.POST['psw']
        Password1 = request.POST['psw-repeat']
        if Password1 == Password:
            user = Register(Username=Username, Email=Email, Mobile_number=Mobile_number, Password=Password)
            user.save()
            messages.success(request, 'User is Registered Successfully!')
            subject = "Welcome to my website!"
            message = f'hi {Username} , thanks for registering yourself to our website, this is a welcome email, hope you will enjoy using it!'
            sender_email = settings.EMAIL_HOST_USER
            receiver_email = [Email]
            send_mail(subject, message, sender_email, receiver_email, fail_silently=True)
        else:
            messages.error(request, 'Passwords don\'t match!, please try to register again')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':

        Mobile_number = request.POST['mobile']

        sendotp(
            Mobile_number
        )
    else:
        messages.error(request, 'phone number is not valid!')
    return render(request, 'login.html')


def sendotp(phone_number):
    try:
        otp = random.randint(1000, 9999)
        url = f"https://2factor.in/API/V1/{settings.api_key}/SMS/{phone_number}/{otp}"
        response = requests.get(url)
        return otp
    except Exception as e:
        print(e)
        return None
