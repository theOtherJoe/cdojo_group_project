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
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters!"
        if postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords do not match!"
        return errors

class GameManager(models.Manager):
    def game_validator(self, postData):
        errors = {}
        if len(postData['game_title']) < 2:
            errors['game_title'] = "Game title must be at least 2 characters!"
        if len(postData['game_description']) < 2:
            errors['game_description'] = "Description is required and must be at least 2 or more characters!"
        if not postData['game_date']:
            errors['game_date'] = "Release date is required!"
        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['game_review']) < 2:
            errors['game_review'] = "Please provide your review and it must be at least 2 or more characters long."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # games = []
    # reviews = []

class Game(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    publisher = models.ForeignKey(User, related_name="games", on_delete=models.CASCADE)
    release_date = models.DateField()
    game_image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GameManager()
    # reviews = []

class Review(models.Model):
    review = models.TextField()
    reviewer = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()