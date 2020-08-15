import json

from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.http import JsonResponse

# Create your views here.
@login_required
def categorize(request):
    try:
        personal_finances = Finance.objects.get(user=request.user)
        percentages = Percentages.objects.get(id=1)
    except:
        personal_finances = None
        percentages = None

    if request.method == "POST":
        income = Decimal(request.POST["income"])

        if personal_finances == None:
            income1 = Finance(user=request.user, income=income)
            income1.save()
        else:
            personal_finances.income = income
            personal_finances.save()
        
            
        

    # Setting default percentages
    tax_p = percentages.tax_rate
    emergency_p = percentages.emergency
    insurance_p = percentages.insurance
    pension_p = percentages.pension
    spending_p = Decimal(1- tax_p -emergency_p -insurance_p -pension_p)
    

    # Calculating respective categories
    personal_finances.tax = round(tax_p * personal_finances.income, 2)
    personal_finances.emergency = round(emergency_p * personal_finances.income, 2)
    personal_finances.insurance = round(insurance_p * personal_finances.income, 2)
    personal_finances.pension = round(pension_p * personal_finances.income, 2)
    personal_finances.spending = round(spending_p * personal_finances.income, 2)
    personal_finances.save()

    return render(request, "finance/finances.html", {
        "finances": personal_finances,
        "percentages": percentages
    })

@csrf_exempt
@login_required
def edit(request):
    if request.method == "POST":

        # Saving JS form data
        emergency = int(request.POST.get('emergency'))
        insurance = int(request.POST.get('insurance'))
        pension = int(request.POST.get('pension'))
        spending = int(request.POST.get('spending'))

        percentages = Percentages.objects.get(user=request.user)
        
        if percentages != None:

            # Updating the DB
            percentages.emergency = emergency
            percentages.insurance = insurance
            percentages.pension = pension
            percentages.spending = spending
            percentages.save()

            return JsonResponse({}, status=201)

        else: 
            return render(request, "finance/error.html")

    return HttpResponseRedirect(reverse("categorize"))

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

    return render(request, "finance/login.html")