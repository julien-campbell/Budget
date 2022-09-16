from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/index/')

        else:
                messages.add_message(request, messages.INFO, 'Wrong Password/Username')       
                return redirect('/')     
    else:
        return render(request, 'home/login.html')


def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email'] 

        if password1 ==password2:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.INFO, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.add_message(request, messages.INFO, 'email taken') 
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                return redirect('/')
            

        else:    
            messages.add_message(request, messages.INFO, 'Password not matching')
            return redirect('register') 
    else:

        return render(request, 'home/register.html')


def log_out(request):
    logout(request)
    return redirect('/')

def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        if User.objects.filter(email=email).exists():
            send_mail(
                'Reset Password',
                'Click the following link to change password: \n http://127.0.0.1:8000/password_reset_form',
                'budgettracker1998@gmail.com',
                [f'{email}'],
                fail_silently=False,
            )
            return redirect('reset_password_sent') 

        else:
                messages.add_message(request, messages.INFO, 'This email is not registered')       
                return redirect('reset_password')     
    else:
        return render(request, 'home/reset_password.html')

def reset_password_sent(request):
    return render(request, 'home/reset_password_sent.html')

def password_reset_form(request):
    if request.method =='POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 ==password2:
            user = request.user
            user.set_password(password1)
            user.save();
            return redirect('/')
            

        else:    
            messages.add_message(request, messages.INFO, 'Password not matching')
            return redirect('password_reset_form') 
    else:

        return render(request, 'home/password_reset_form.html')
