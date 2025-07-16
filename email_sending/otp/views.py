from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model,login,logout
from django.contrib.auth.decorators import login_required
import random
from django.contrib import messages
from .emailer import sendOtpToEmail
User = get_user_model()

# Create your views here.
def login_page(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        user_obj = User.objects.filter(phone_number = phone_number)
        if not user_obj.exists():
            return redirect('/')
        email = user_obj[0].email
        otp = random.randint(1000,9999)
        user_obj.update(otp = otp)
        subject = "Login with OTP"
        message = f"Your OTP is {otp}"
        sendOtpToEmail(email=email , subject=subject , message= message)
        return redirect(f'/check-otp/{user_obj[0].id}/')
    return render(request , 'login_page.html')

def check_otp(request , user_id):
    if request.method == "POST":
        otp = request.POST.get('otp')
        user_obj = User.objects.get(id = user_id)
        if int(otp) == user_obj.otp:
            login(request , user_obj)
            return redirect('/dashboard/')
        messages.error(request , 'Error: Invalid OTP')
        return redirect(f'/check-otp/{user_obj.id}/')
    return render(request , 'check_otp.html')
@login_required(login_url="/")
def dashboard(request):
    return render(request , 'dashboard.html')

@login_required(login_url="/")
def logout_page(request):
    logout(request)
    return redirect('/')