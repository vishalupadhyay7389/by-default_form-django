from django.urls import path
from .import views

urlpatterns = [
    path('student/',views.showdata , name='student'),
    
]