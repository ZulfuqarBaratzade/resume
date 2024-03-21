from django.urls import path
from resume.views import index



urlpatterns = [
    path('',index, name='index'),
]