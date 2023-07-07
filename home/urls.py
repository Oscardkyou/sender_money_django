from django.urls import path, include
from . import views

urlpatterns = [
    path(''),
    path('home/', include('home.urls')),
]
