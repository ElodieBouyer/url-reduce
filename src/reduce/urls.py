from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.add, name='add_url'),
    path('add-url/', views.add, name='add_url'),
    path('api/add', api.add, name='api_add'),
]
