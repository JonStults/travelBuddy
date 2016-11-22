from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45, null=True, blank=True)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Location(models.Model):
    destination = models.CharField(max_length=45, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.ForeignKey(Users, null=True, blank=True)
    start_date = models.CharField(max_length=45, null=True, blank=True)
    end_date = models.CharField(max_length=45, null=True, blank=True)

class Join(models.Model):
    user_id = models.ForeignKey(Users)
    location_id = models.ForeignKey(Location)


# Create your models here.
