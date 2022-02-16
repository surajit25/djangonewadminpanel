import email
from django.db import models
from django.contrib import admin

class Contact(models.Model):

    name = models.CharField(max_length=200,default="",null=True,blank=True)
    email = models.CharField(max_length=200,default="",null=True,blank=True)

    def __str__(self) -> str:
        return self.name


admin.site.register(Contact)