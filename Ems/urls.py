from django.contrib import admin
from django.urls import path
from Ems import views

urlpatterns = [
    path("index/",views.home,name = "home"),
    path('login/', views.Login.as_view(), name='login'),
    path('', views.index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('add/', views.add.as_view(), name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('logout/',views.logout_view,name='logout'),
    # path('edit/', views.Edit.as_view(), name='edit'),
    path('update/<int:id>/', views.APPUpdateView.as_view(), name='update'),
]