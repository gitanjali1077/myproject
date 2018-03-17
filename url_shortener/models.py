from django.db import models

# Create your models here.

class urls(models.Model):
    long_url = models.CharField(max_length=400)
    short_url = models.CharField(max_length=50,unique=True)
    count = models.IntegerField(default=0,blank=True)
    status = models.CharField(max_length=400,blank=True)
    status_codes = models.CharField(max_length=400,blank=True)
    
    def __str__(self):
        return self.short_url
