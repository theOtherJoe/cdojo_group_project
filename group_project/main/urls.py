from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('home', views.homepage),
    path('add', views.add),
    path('add_game', views.add_game),
    path('create', views.home_create),
    path('dashboard', views.dashboard),
    path('log', views.log_user),
    path('review', views.review),
    path('add_review', views.add_review),
    path('logout', views.logout),
]