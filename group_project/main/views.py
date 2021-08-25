from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def home(request):
    return render(request, "index.html")

def homepage(request):
    return render(request, "log_reg.html")

def home_create(request):
    errors = User.objects.basic_validator(request.POST)
    user= User.objects.filter(email=request.POST['email'])
    if user:
        messages.error(request, "Email is already taken!")
        return redirect('/')
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user=User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=pw_hash)
        request.session['log_user_id'] = new_user.id
    return redirect('/dashboard')

def log_user(request):
    user= User.objects.filter(email=request.POST['email'])
    if user:
        logged_user= user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['log_user_id'] = logged_user.id
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid Email or Password!', extra_tags='invalid')
            return redirect('/home')
    messages.error(request, "Email does not exist")
    return redirect('/home')

def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    print('Dashboard')
    context = {
        'user': User.objects.get(id=request.session['log_user_id']),
        'all_games': Game.objects.all(),
        'all_reviews': Review.objects.all()
    }
    return render(request, 'dashboard.html', context)

def add(request):
    if "log_user_id" not in request.session:
        return redirect('/')
    context = {
        "user_id": User.objects.get(id=request.session['log_user_id']),
    }
    return render(request, 'add.html', context)

def add_game(request):
    if "log_user_id" not in request.session:
        return redirect('/')
    if request.method == "POST":
        current_user = User.objects.get(id=request.session['log_user_id'])
        new_game = Game.objects.create(
            title = request.POST['game_title'], 
            description = request.POST['game_description'],
            release_date = request.POST['release_date'],
            game_image = request.FILES['game_image'],
            publisher = current_user
            )
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')

def review(request, rev_id):
    if "log_user_id" not in request.session:
        return redirect('/')
    context = {
        'current_game': Game.objects.get(id=rev_id)
    }
    return render(request, 'review.html', context)

def add_review(request, rev_id):
    if "log_user_id" not in request.session:
        return redirect('/')
    if request.method == "POST":
        current_user = User.objects.get(id=request.session['log_user_id'])
        current_game = Game.objects.get(id=rev_id)
        new_review = Review.objects.create(
            game_review = request.POST['game_review'],
            reviewer = current_user,
            reviews_for_game = current_game
            )
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')

def show_reviews(request, game_id):
    if "log_user_id" not in request.session:
        return redirect('/')
    game = Game.objects.get(id=game_id)
    context = {
        'current_user': User.objects.get(id=request.session['log_user_id']),
        'current_game': Game.objects.get(id=game_id),
        'reviews_for_game': game.reviews.all()
    }
    return render(request, 'show_reviews.html', context)