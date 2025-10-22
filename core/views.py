from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .models import Converts
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone

import csv

# Create your views here.


def post(self, request, *args, **kwargs):
    # Handle POST requests if needed
    pass


def error_404_view(request, exception):
    return render(request, "404.html")


def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.check_password(password):
                logged_user = auth.authenticate(username=username, password=password)
                if logged_user is not None:
                    auth.login(request, logged_user)
                    if user.last_login == None:
                        return HttpResponseRedirect(reverse("core:change_password"))
                    else:
                        return HttpResponseRedirect(reverse("core:dashboard"))
                else:
                    messages.error(request, "User does not exist")
                    return HttpResponseRedirect(reverse("core:admin_login"))

            else:
                messages.error(request, "Incorrect Password")

        else:
            messages.error(request, "User does not exist")
            return HttpResponseRedirect(reverse("core:admin_login"))

    return render(request, "core/admin_login.html", {})


@login_required
def dashboard(request):
    print(request.user)
    return render(request, "core/dashboard.html", {})


@login_required
def data_table(request):
    converts = Converts.objects.all()
    coppe = 0
    date_to_owner = {}
    each_dates = []
    dict_date = []
    today = datetime.now().date()
    print("*****************************\n")
    print(f"General Date: {today} \n")
    print("*****************************")
    for i in range(0,len(converts)):
        each_dates.append(converts[i].date)
    date_set = list(set(each_dates))
    date_set = sorted(date_set, reverse=True)
    for i in range(0,len(converts)):
        for j in range(0, len(date_set)):
            coppe = list(Converts.objects.filter(date = date_set[j]))   
            date_to_owner[date_set[j]] = coppe
    print(date_set)
    lenConvert = len(converts)
    return render(
        request,
        "core/datatable.html",
        {"converts": converts, "date_data" : date_to_owner},
    )


@login_required
def profile(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["adminpassword"]

        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username} already exists ")
        else:
            User.objects.create_user(username=username, password=password)
            return HttpResponseRedirect(reverse("core:profile"))
    return render(request, "core/profile.html", {})


@login_required
def change_password(request):
    if request.method == "POST":
        oldpassword = request.POST["oldpassword"]
        newpassword = request.POST["newpassword"]
        confirmpassword = request.POST["confirmpassword"]

        if request.user.check_password(oldpassword):
            if newpassword == confirmpassword:
                request.user.set_password(newpassword)
                request.user.save()
                return HttpResponseRedirect(reverse("core:dashboard"))
    return render(request, "core/changepass.html", {})


@login_required
def manageadmin(request):
    user = User.objects.filter(is_superuser=False)
    return render(request, "core/manageadmin.html", {"user": user})

@login_required
def delete(request):
    if len(Converts.objects.all()) != 0:
        Converts.objects.all().delete()
        return HttpResponseRedirect(reverse("core:data_table"))
    else:
        return HttpResponseRedirect(reverse("core:data_table"))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("core:admin_login"))

@login_required
def export(request):
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(["Fullname", "Email", "Phone_number", "Address", "Prayer_point"])
    for convert in Converts.objects.all().values_list(
        "Fullname", "Email", "Phone_number", "Address", "Prayer_point"
    ):
        writer.writerow(convert)
    response["Content-Disposition"] = 'attachment; filename="converts.csv"'

    return response
