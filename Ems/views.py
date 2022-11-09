from django.shortcuts import render

from Employee_Management_System import settings
from scrape import break_login_logout
from Ems.models import *
from skpy import *

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

sk = Skype(settings.SKYPE_EMAIL, settings.SKYPE_PASS)

def home(request):

    log_time = break_login_logout()
    def log():
        for i in log_time:

            # lis = []
            if i.content.lower() == "break":
                # print("\n","break : ",i)
                a = str(i)
                b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                time= str(a.split("Time")[1].split()[2:3])
                time=time [2:10]
                contact = sk.contacts[b]
                name = contact.name
                print("break:",name,date,time)



            # lis = []
            if i.content.lower().replace(" ","") == "goodmorning":
                # print("\n","login : ",i)
                a = str(i)
                b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                time= str(a.split("Time")[1].split()[2:3])
                time=time [2:10]
                contact = sk.contacts[b]
                name = contact.name
                print("login:",name,date,time)


            # lis = []
            if i.content.lower().replace(" ","") == "backtowork":
                # print("\n","back to work : ", i)
                a = str(i)
                b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                time= str(a.split("Time")[1].split()[2:3])
                time=time [2:10]
                contact = sk.contacts[b]
                name = contact.name

                print("back to work:",name,date,time)




            # lis = []
            if "what did you do today" in i.content.lower():
                # print("\n","logout : ",i)
                a = str(i)
                b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                time= str(a.split("Time")[1].split()[2:3])
                time=time [2:10]
                contact = sk.contacts[b]
                name = str(contact.name)
                print("logout:",name,date,time)





    log()




    return render(request,"home.html")









class Login(View):
    def get(self, request):
        return render(request, 'log/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            status=user.check_password(password)
            if status:

                  return redirect('/index/')
            else:

                return render(request, 'log/login.html', {'message': "Password  incorrect"})
        except:
            message="Please check username"
            return render(request, 'log/login.html',{'message':message})




def index(request):
    a = Employee.objects.all()
    return render(request, 'log/index.html',{'a':a})

def employee(request):
    a=Employee.objects.all()
    return render(request, 'log/index2.html',{'a':a})

def delete(request,id):
   b= Employee.objects.get(id=id)
   b.delete()
   return redirect('/employee/')


class add(View):
    def get(self, request):
        return render(request, 'log/add2.html')
    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        employee = Employee.objects.create(employee_id=id,name=name,email=email)
        employee.save()
        return redirect('/employee/')







