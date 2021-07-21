from django.urls import path
from . import views


urlpatterns = [
    path('', views.image, name='images'),
    path('image/<str:pk>/', views.viewImage, name='image-view'),
    path('add/', views.addImage, name='new-image'),
]