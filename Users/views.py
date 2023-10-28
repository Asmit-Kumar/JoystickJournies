from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from JoystickJournies.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from . import forms
from django.core.mail import send_mail

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('../login/')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../home/')  
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


@login_required(login_url= '../login/')
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('../home/')
    return render(request, 'users/logout.html', {})


'''@login_required(login_url= '../login/')
def user_logout(request):
    logout(request)
    return redirect('../home/')


@login_required(login_url= '../login/')
def logout_view(request):
    return render(request, 'users/logout.html', {})'''


@login_required(login_url= '../login/')
def user_dashboard(request):
    current_user = request.user
    dict = {'user': current_user}
    return render(request, 'users/dashboard.html', dict)


@login_required(login_url='../login/')
def edit_profile(request):
    curr_user = User.objects.get(username = request.user)

    if request.method == 'POST':
        form = UserChangeForm(instance = curr_user, data = request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_joined = request.user.date_joined
            post.save()
            return redirect('../profile/')
    else:
        form = UserChangeForm(instance = curr_user)
    
    dict = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'users/edit_profile.html', dict)


def DynamicUserView(request, uname):
    vuser = User.objects.get(username = uname)
    curr_user = request.user
    context = {
        'user': vuser,
        'cuser': request.user,
    }
    if str(uname) == str(curr_user):
        return redirect('../../profile/')
    return render(request, 'users/profile.html', context)


@login_required(login_url='../login/')
def feedback(request):
    sub = forms.Feedback()
    if request.method == 'POST':
        sub = forms.Feedback(request.POST)
        print(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        subject = 'Welcome to Joystick Journies'
        message = 'Good Efforts and Hope you are enjoying our content.'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

        return render(request, 'users/success.html', {'recepient': recepient})
    return render(request, 'users/index.html', {'form':sub})
