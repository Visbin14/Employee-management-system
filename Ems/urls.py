from django.contrib import admin
from django.urls import path
from Ems import views
# from . import views
# from .views import APPUpdateView

urlpatterns = [
    path("index/",views.home,name = "home"),
    path('login/', views.Login.as_view(), name='login'),
    path('', views.index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('add/', views.add.as_view(), name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('logout/',views.logout_view,name='logout'),
    # path('edit/', views.Edit.as_view(), name='edit'),
    path('update/<int:id>/<date>', views.editdetails, name='update'),
    # path('update1/<int:id>/', views.ModelForm.as_view(), name='update1'),

]