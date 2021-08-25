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
    path('review/<int:rev_id>', views.review),
    path('add_review/<int:rev_id>', views.add_review),
    path('show_reviews/<int:game_id>', views.show_reviews),
    path('logout', views.logout),
]