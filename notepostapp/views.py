from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.contrib.auth.models import User

from django.contrib import messages
from .models import Notepost



@login_required
def index(request):
    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            Notepost.objects.create(text=text, user=request.user)
        return redirect('/')

    noteposts = Notepost.objects.filter(user=request.user)
    context = {
        'noteposts': noteposts
    }
    return render(request, 'notepostapp/index.html', context)


@login_required
def deleteNotepost(request, id):
    get_object_or_404(Notepost, id=id, user=request.user).delete()
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            authLogin(request, user)
            messages.add_message(request, messages.SUCCESS, "Successfully Logged in.")
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, "Credentials are not valid.")
            return redirect('login')

    return render(request, 'notepostapp/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 != password2:
            messages.add_message(request, messages.ERROR, "Passwords didn't match")
            return redirect("register")

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)

        authLogin(request, user)
        return redirect('index')

    return render(request, 'notepostapp/register.html')


def logout(request):
    authLogout(request)
    return redirect('login')
