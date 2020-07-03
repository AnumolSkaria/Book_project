from django.contrib import admin
from django.urls import path, include
from Consumer.views import *

urlpatterns = [
    path('registration/',consumerRegistration,name='reg'),
    path('login/',consumerLogin,name='login'),
    path('consumerhome/',consumerHome,name='home'),
    path('home/',home,name='consumerhome'),
    path('buy/<int:pk>',buyNow,name='buy'),
]
