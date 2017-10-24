from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User
import re 
import bcrypt


class PetManager(models.Manager):
    def validate_review(self, post_data):
        value = {"errors": [], "status": False}

        if len(post_data['name']) < 1:
            value["errors"].append("please enter a pet name")
            value["status"] = True

        if len(post_data['type']) < 1:
            value["errors"].append("please enter a pet type")
            value["status"] = True

        return value

class Pet(models.Model):
    name =  models.CharField(max_length=255)
    pettype =  models.CharField(max_length=255)
    users = models.ForeignKey(User, related_name="pets")
    objects = PetManager()

