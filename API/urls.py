
from django.urls import path
from .views import *
urlpatterns = [
    path('',view=index , name="index")
]
