from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('', login_view, name='login'),
    path('entry/', entry_dash, name='entry_home'),
]
