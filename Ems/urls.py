from django.contrib import admin
from django.urls import path
from Ems import views

urlpatterns = [
    path("",views.home,name = "home"),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('add/', views.add.as_view(), name='add'),
]