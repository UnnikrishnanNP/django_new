from django.urls import path
from .views import *


app_name = 'leads'

urlpatterns = [
    path('',lead_list),    
    path('<pk>/',lead_details)    
]