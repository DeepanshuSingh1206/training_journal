from django.urls import path
from . import views

app_name = "journal"
urlpatterns = [path("", views.index, name="index"),
                path("login", views.login, name = "login"),
                path("signup", views.signup, name = "signup"),
                path("delete_exercise", views.delete_exercise, name="delete_exercise"),
                path('<str:user_name>/', views.dashboard, name='dashboard'),]