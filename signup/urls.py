from django.urls import path
from signup import views

app_name = "signup"

urlpatterns = [
    path("", views.signup, name="signup"),
    path("convert/", views.convert, name = "convert"),
]
