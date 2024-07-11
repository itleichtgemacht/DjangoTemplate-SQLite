from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),    #  https://localhost:8000/helloworld wird mit der View views.hello verbunden
]
