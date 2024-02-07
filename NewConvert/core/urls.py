from django.urls import path 
from core import views

app_name = "core"
urlpatterns = [
    path("dashboard/", views.dashboard, name = "dashboard"),
    path("datatable/", views.data_table, name = "data_table"),
    path("profile/", views.profile, name = "profile"),
    path("changepassword/", views.change_password, name = "change_password"),
    path("logout/", views.logout, name = "logout")
]
