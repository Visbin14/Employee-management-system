from django.shortcuts import render

from Employee_Management_System import settings
from scrape import break_login_logout
from Ems.models import *
from Ems.Log import logged
from skpy import *

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

from datetime import datetime

sk = Skype(settings.SKYPE_EMAIL, settings.SKYPE_PASS)


def home(request):
    log_time = break_login_logout()

    def log():
        for i in log_time:
            if i.content.lower() == logged.get('Break'):
                print(i,"////////////////////")
                print("entering to break")
                a = str(i)
                b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                print(b,"-------------------------")
                date = a.split("Time")[1].split()[1:2]
                time = str(a.split("Time")[1].split()[2:3])
                time = time[2:10]
                contact = sk.contacts[b]
                name = contact.name


                obj = Employee.objects.get(name=name)
                log,status = Log_status.objects.get_or_create(Emp=obj, Log="break", Time=time)
                if status:
                    logged_time = Logged_Time.objects.create(Employee=obj, Date=date[0])
                    logged_time.Log.add(log)

            if i.content.lower().replace(" ", "") == logged.get('Login'):
                print("entering to Login")
                a = str(i)
                b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                time = str(a.split("Time")[1].split()[2:3])
                time = time[2:10]
                contact = sk.contacts[b]
                name = contact.name
                obj1 = Employee.objects.get(name=name)

                log,status = Log_status.objects.get_or_create(Emp=obj1, Log="login", Time=time)
                # log.save()
                if status:
                    logged_time = Logged_Time.objects.create(Employee=obj1, Date=date[0])
                    logged_time.Log.add(log)

            if i.content.lower().replace(" ", "") == logged.get('Back_to_work'):
                print("entering to back to work")
                a = str(i)
                b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                time = str(a.split("Time")[1].split()[2:3])
                time = time[2:10]
                contact = sk.contacts[b]
                name = contact.name
                obj2 = Employee.objects.get(name=name)

                log,status = Log_status.objects.get_or_create(Emp=obj2, Log="back to work", Time=time)
                # log.save()
                if status:
                    logged_time = Logged_Time.objects.create(Employee=obj2, Date=date[0])
                    logged_time.Log.add(log)

            if logged.get('Logout') in i.content.lower():
                print("entering to Loginout")
                a = str(i)
                b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                print(date,"//////////")
                time = str(a.split("Time")[1].split()[2:3])
                time = time[2:10]
                contact = sk.contacts[b]
                name = contact.name
                obj3 = Employee.objects.get(name=name)
                print(obj3.name,"////")
                log,status = Log_status.objects.get_or_create(Emp=obj3, Log="logout", Time=time)
                # log.save()
                if status:
                    logged_time = Logged_Time.objects.create(Employee=obj3, Date=date[0])
                    logged_time.Log.add(log)

    log()

    return render(request, "home.html")


class Login(View):
    def get(self, request):
        return render(request, 'log/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            status = user.check_password(password)
            if status:

                return redirect('/index/')
            else:

                return render(request, 'log/login.html', {'message': "Password  incorrect"})
        except:
            message = "Please check username"
            return render(request, 'log/login.html', {'message': message})


def index(request):
    employess = Employee.objects.all()
    # time=Logged_Time.objects.all()
    # from datetime import datetime
    # from datetime import date, timedelta
    #
    # today = date.today()
    # yesterday = today - timedelta(days=1)
    # print("yesterday",yesterday)
    # logged_list = []
    # d = {}
    # for employeee in employess:
    #     logged_time_list = Logged_Time.objects.filter(Employee=employeee,Date=yesterday)
    #     for logged_time in logged_time_list:
    #         if logged_time.Employee.name not in d:
    #             d[logged_time.Employee.name] = logged_time_list
    #             logged_list.append(d)
    #
    #         else:
    #             continue

    Emp_work_hours={}
    # print(">>>>>>>",logged_list)
    emp_obj= Employee.objects.all()
    li= []
    for i in emp_obj:
        li.append(i.name)
    for names in li:
        print(names)
        b= names
        import datetime
        x = datetime.datetime(2022, 11, 10)
        # a=Log_status.objects.filter(Log="login",Emp__name=b),
        # print(a,"<////////////////////////////////")

        login_obj=Logged_Time.objects.filter(Employee__name=b,Date=x)
        login_time= None
        logout_time= None
        logout_break_time = None
        logout_back_to_work = None
        for i in login_obj:


            for j in i.Log.all():
                print("Date:", i.id)
                print(i.Date,j.Log,j.Time,"[][][][")
                if j.Log == "login":
                    login_time = j.Time
                if j.Log == "logout":
                    logout_time = j.Time
                if j.Log == "break":
                    logout_break_time = j.Time
                if j.Log == "back to work":
                    logout_back_to_work = j.Time
        print("login_time",login_time)
        print("logout_time", logout_time)
        print("logout_break_time", logout_break_time)
        print("logout_back_to_work", logout_back_to_work)
        if login_time and logout_time:
            t1 = datetime.datetime.strptime(str(login_time), "%H:%M:%S")
            t2 = datetime.datetime.strptime(str(logout_time), "%H:%M:%S")

            delta = t2 - t1
            print(delta,"/////////")
        if logout_break_time and logout_back_to_work:
            print((">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"))
            b1= datetime.datetime.strptime(str(logout_break_time), "%H:%M:%S")
            b2= datetime.datetime.strptime(str(logout_back_to_work), "%H:%M:%S")

            show = b2 - b1
            print(show, "/////////")

            total_working_hours= delta-show
            print(total_working_hours,"444444444444444444444444444444444444444444")
        Emp_work_hours[names] = total_working_hours




        # break

    print("Emp_work_hours",Emp_work_hours)
    return render(request, 'log/index.html', {'data': Emp_work_hours.items()})

def employee(request):
    a = Employee.objects.all()
    return render(request, 'log/index2.html', {'a': a})


def delete(request, id):
    b = Employee.objects.get(id=id)
    b.delete()
    return redirect('/employee/')


class add(View):
    def get(self, request):
        return render(request, 'log/add2.html')

    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        employee = Employee.objects.create(employee_id=id, name=name, email=email)
        employee.save()
        return redirect('/employee/')
