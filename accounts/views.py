from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                password=pass1)

                user.save()
                print("User created")

                return redirect('accounts:home')
        else:
            messages.error(request, "Enter same passwords")
            return redirect('accounts:register')

    else:
        #form = RegistrationForm()
        #profileform = UserProfileForm()
        return render(request, 'accounts/register.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("Login Successfull")
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounts:home')

        else:
            messages.error(request, "Login Failed, Enter correct credentials")
            return redirect('accounts:login')

    else:

        return render(request, 'accounts/login.html')


def homepg(request):
    return render(request, 'accounts/homepg.html')


def logoutuser(request):

    logout(request)
    print("Logout successful")
    return redirect('/accounts/login/')
