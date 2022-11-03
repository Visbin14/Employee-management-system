from django.contrib import admin
from Ems.models import Employee,Log_status,Logged_Time

# Register your models here.
admin.site.register(Employee)
admin.site.register(Log_status)
admin.site.register(Logged_Time)