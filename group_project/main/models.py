from django.db import models
import re

from django.db.models.deletion import CASCADE

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters!"
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters!"
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    games = models.ImageField(null=True, blank=True, upload_to="images/")
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Game(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    user_review = models.ForeignKey(User, related_name="game_review", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)