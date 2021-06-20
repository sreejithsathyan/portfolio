from django.db import models
# Create your models here.
class Company(models.Model):
    name = models.TextField()
    slug = models.SlugField(unique=True)
    details = models.TextField(null = True,blank = True)
