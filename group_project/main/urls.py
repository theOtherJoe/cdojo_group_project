from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('create', views.home_create),
    path('dashboard', views.dashboard),
    path('log', views.log_user),
    path('logout', views.logout),
]