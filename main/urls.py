from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('contacts/', views.contacts, name="contacts"),
    path('services/', views.services, name="services"),
    path('repair/', views.repair, name="repair"),
    path('projects/', views.projects, name="projects"),
    path('reviews/', views.reviews, name="reviews"),
    path('designing/', views.designing, name="designing"),

    path('about/', views.about, name="about"),
    path('register/', views.UserCreations.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('cards<int:pk>/', views.cards, name="cards")
]
