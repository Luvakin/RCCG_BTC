from django.db import models

# Create your models here.
# Collecting the converts data

class Converts(models.Model):
    Fullname = models.CharField(max_length = 120)
    Email = models.EmailField(blank= True, null = True)
    Phone_number = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 150)
    Prayer_point = models.CharField(max_length = 300)

    def __str__(self):
        return self.Fullname
    
    class Meta:
        verbose_name_plural = "Converts"
