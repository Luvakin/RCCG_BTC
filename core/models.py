from django.db import models
from datetime import datetime

# Create your models here.
# Collecting the converts data

class Converts(models.Model):
    Fullname = models.CharField(max_length = 120)
    Email = models.EmailField(blank= True, null = True)
    Phone_number = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 150)
    Prayer_point = models.CharField(max_length = 300)
    date = models.DateField(default = datetime.now().date())

    print(datetime.now().date())
    def __str__(self):
        return self.Fullname
    
    def get_date(self):
        pass

    class Meta:
        verbose_name_plural = "Converts"
