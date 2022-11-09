from django.contrib import admin
from django.urls import path
from Ems import views

urlpatterns = [
    path("",views.home,name = "home"),
    path('login/', views.Login.as_view(), name='login'),
    path('index/', views.index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('add/', views.add.as_view(), name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
]