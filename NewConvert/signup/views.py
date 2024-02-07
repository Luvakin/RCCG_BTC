from django.shortcuts import render

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
        
    return render (request, "signup/convert.html", context = {})