from django.db import models
import re
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

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

class GameManager(models.Manager):
    def game_validator(self, postData):
        errors = {}
        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # games_uploaded = []
    # reviews_made = []

class Game(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    publisher = models.ForeignKey(User, related_name="games_uploaded", on_delete=models.CASCADE)
    release_date = models.DateField()
    game_image = models.ImageField(null=True, blank=True, upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GameManager()
    # reviews = []

class Review(models.Model):
    game_review = models.TextField()
    reviewer = models.ForeignKey(User, related_name="reviews_made", on_delete=models.CASCADE)
    reviews_for_game = models.ForeignKey(Game, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()