from django.contrib import admin
from .models import Converts
from import_export import resources


# Register your models here.
class convertResource(resources.ModelResource):
    class Meta:
        model = Converts
        fields = ("Fullname", "Email", "Phone_number", "Address", "Prayer_point")
        export_order = ("Fullname", "Email", "Phone_number", "Address", "Prayer_point")


admin.site.register(Converts)
