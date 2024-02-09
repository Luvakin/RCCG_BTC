from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import UserForm
# Create your views here.

def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username = username).exists():
            user = User.objects.get(username = username)
            if user.check_password(password):
                logged_user = auth.authenticate(username = username, password = password)
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


    return render(request, "core/admin_login.html",{})
def dashboard(request):
    return render(request, "core/dashboard.html", {})

def data_table(request):
    return render (request, "core/datatable.html", {})

def profile(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["adminpassword"]
        
        if User.objects.filter(username = username).exists():
            messages.error(request, f"Username '{username} already exists ")
        else:
            User.objects.create_user(username = username, password = password)
            return HttpResponseRedirect(reverse("core:profile"))
    return render (request, "core/profile.html", {})

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
    return render (request, "core/changepass.html", {})

def manageadmin(request):
    user = User.objects.filter(is_superuser = False)
    return render (request, "core/manageadmin.html", {"user" : user})
def logout(request):
    pass    