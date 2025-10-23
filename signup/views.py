from django.shortcuts import render, redirect
from core.models import Converts
from datetime import datetime
# Create your views here.

def signup(request):
    return render(request, "signup/index.html", context = {})

def convert(request):
    if request.method == "POST":
        Fullname = request.POST["fullname"]
        Email = request.POST.get("email")
        Phone = request.POST["phone_number"]
        Address = request.POST["address"]
        Prayer = request.POST["prayer"]

        convert = Converts(Fullname = Fullname, Email = Email, Phone_number = Phone, Address = Address, Prayer_point = Prayer)
        convert.save()


        return redirect("signup:thankyou")
    return render (request, "signup/convert.html", context = {})







def thankyou(request):
    return render(request, "signup/done.html", context = {})
