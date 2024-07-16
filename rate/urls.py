from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/calc_gross_sal', views.calculate_net_pay)
]