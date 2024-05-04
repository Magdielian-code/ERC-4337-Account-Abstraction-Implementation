from django.urls import path
from . import views

urlpatterns = [
    path('create-account/', views.create_account, name='create-account'),
]