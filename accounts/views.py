from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == "POST":
        banana = UserCreationForm(request.POST)
        if banana.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
            login(request, user)
            return redirect("home")
    else:
        banana = UserCreationForm()
    context = {
        "form": banana,
    }
    return render(request, "registration/signups.html", context)
