from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('', login_view, name='login'),
    path('entry/', entry_dash, name='entry_home'),
    path('master/', entry_page, name='master'),
    path('export/', export_data_csv, name='export_data_csv'),
    path('import/', import_data_csv, name='import_data_csv'),
    path('go_entry', entry_data, name='entry_data'),
]
