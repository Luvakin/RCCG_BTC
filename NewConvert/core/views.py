from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "core/dashboard.html", context={})

def data_table(request):
    return render (request, "core/datatable.html", context={})

def profile(request):
    return render (request, "core/profile.html", context={})

def change_password(request):
    return render (request, "core/changepass.html", context={})

def logout(request):
    pass    