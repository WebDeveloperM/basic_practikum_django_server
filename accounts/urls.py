from django.urls import path
from .views import *

urlpatterns = [
    path('sigup/', SignUpView.as_view(), name='signup')
    ]