from django.urls import path
from  . import views

# URLCONFIGURATION
urlpatterns = [
    path('hello/', views.say_hello)
]