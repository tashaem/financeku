from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from django.shortcuts import HttpResponse, HttpResponseRedirect, render

# Create your views here.
@login_required
def categorize(request):
    if request.method == "POST":
        income = request.POST["income"]

        try:
            personal_finances = Finance.objects.get(user=request.user)
        except:
            personal_finances = None

        if personal_finances == None:
            income1 = Finance(user=request.user, income=income)
            income1.save()

    return render(request, "finance/finances.html", {
        "finances": personal_finances
    })
            
@login_required
def index(request):

    if request.user.is_authenticated:
        return render(request, "finance/index.html")

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("loginpage"))

def loginpage(request):
    if request.method == "POST":
        try:
            # Get email and pass from form
            username = request.POST["username"]
            password=request.POST["password"]

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))

        except IntegrityError:
            return render(request, "finance/error.html")

    return render(request, "finance/login.html")

@login_required
def logoutpage(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginpage"))

def register(request):

    if request.method == "POST":
        try:
            # Get email and pass from form
            username = request.POST["username"]
            email = request.POST["email"]
            password=request.POST["password"]

            # Update DB
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            return render(request, "finance/error.html")

    return render(request, "finance/register.html")