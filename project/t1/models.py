from django.db import models
from django.contrib import admin

class my_info (models.Model):
    name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 20)
    date_of_birth = models.DateField()

    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length = 20, blank = True)
    other_contacts = models.TextField(blank = True)

    bio = models.TextField()

admin.site.register(my_info)
