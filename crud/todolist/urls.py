from django.urls import path
# from todolist import views
from . import views

urlpatterns = [
    path('', views.create)
]
