from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path(playground, views.say_hello)
]