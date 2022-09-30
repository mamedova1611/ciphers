
from django.urls import path
from .views import *

urlpatterns = [
    path('', FormView.as_view()),
    path('cipher/', CipherView.as_view(), name='cipher')
]
