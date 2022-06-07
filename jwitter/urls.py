from django.urls import path
from .views import dashboard

app_name= 'jwitter'


urlpatterns = [
    path('', dashboard, name='dashboard'),
]
