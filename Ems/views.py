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
import numpy as np
from datetime import datetime

sk = Skype(settings.SKYPE_EMAIL, settings.SKYPE_PASS)


def home(request):
    log_time = break_login_logout()

    def log():
        for i in log_time:
            if i.content.lower() == logged.get('Break'):
                a = str(i)
                b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()

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

                a = str(i)
                b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                time = str(a.split("Time")[1].split()[2:3])
                time = time[2:10]
                contact = sk.contacts[b]
                name = contact.name
                obj1 = Employee.objects.get(name=name)

                log,status = Log_status.objects.get_or_create(Emp=obj1, Log="login", Time=time)

                if status:
                    logged_time = Logged_Time.objects.create(Employee=obj1, Date=date[0])
                    logged_time.Log.add(log)

            if i.content.lower().replace(" ", "") == logged.get('Back_to_work'):

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

                a = str(i)
                b = a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]

                time = str(a.split("Time")[1].split()[2:3])
                time = time[2:10]
                contact = sk.contacts[b]
                name = contact.name
                obj3 = Employee.objects.get(name=name)

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

    Emp_work_hours={}

    emp_obj= Employee.objects.all()
    li= []
    b1=[]
    for i in emp_obj:
        li.append(i.name)
    for names in li:
        print(names)
        b= names
        import datetime
        x = datetime.datetime(2022, 11, 9)
        login_obj=Logged_Time.objects.filter(Employee__name=b,Date=x)
        login_time= None
        logout_time= None
        logout_break_time = None
        logout_back_to_work = None
        br = []
        bk = []



        for i in login_obj:


            for j in i.Log.all():
                print(j,"<<<<<<<<<<<<<<<<<<",j.Time,i.Date)

                if j.Log == "login":
                    login_time = j.Time
                if j.Log == "logout":
                    logout_time = j.Time

                if j.Log == "break":
                    # br.append(j.Log)
                    br.append(j.Time)

                if j.Log=="back to work":
                    # bk.append(j.Log)
                    bk.append(j.Time)


        br_new = sorted(br)
        bk_new = sorted(bk)
        print("br",br)
        print("bk", bk)
        print(br_new,">>>>>>>>>>>>>>")
        print(bk_new,">>>>>>>>>>>?????")

        for br in br_new:
            print(">>>>>>>>>",br)
            total_break=0
            br_string = br .strftime("%H:%M:%S")
            print(br_string,"cccccc")
            bt_index=br_new.index(br)
            try:
                bk_string=bk_new[bt_index].strftime("%H:%M:%S")
                print("br_string",br_string,"bk_string",bk_string)
                b1 = datetime.datetime.strptime(br_string, "%H:%M:%S")
                b2=datetime.datetime.strptime(bk_string, "%H:%M:%S")

                difference= b2 - b1
                wh = difference.total_seconds()/60/60
                print(difference,"break difference")
            except Exception as e:
                print(e)


            # print(d,"???????")

            # b1.append(d)

            # b1=datetime.datetime.strptime(br_string, "%H:%M:%S")
            # b2=datetime.datetime.strptime(bk_string, "%H:%M:%S")
            # print(b2,"<<<")
            # print(b1,">>>")

        # break_time1 =  datetime.datetime.strptime(str(bk_new[0]), "%H:%M:%S") - datetime.datetime.strptime(str(br_new[0]), "%H:%M:%S")
        # break_time2 =  datetime.datetime.strptime(str(bk_new[1]), "%H:%M:%S") - datetime.datetime.strptime(str(br_new[1]), "%H:%M:%S")
        # # d={}
        # # for i in range(len(br_new)):
        # #
        # #     d[str(br_new[i])] =  str(bk_new[i])
        #
        # # k2=br_new[0].strftime("%H:%M:%S")
        # # K1=bk_new[0].strftime("%H:%M:%S")
        # # t1 = datetime.datetime.strptime(str(login_time), "%H:%M:%S")
        # # for br in br_new:
        # #     total_working_hr=0
        # #     k2 = br.strftime("%H:%M:%S")
        #
        #
        #
        #             # logout_break_time = j.Time
        #         # if j.Log == "back to work":
        #         #     logout_back_to_work = j.Time
        # # print("backwork", bw)
        # print("login_time",login_time)
        # print("logout_time", logout_time)
        # # print("logout_break_time", logout_break_time)
        # # print("logout_back_to_work", logout_back_to_work)

        if login_time and logout_time:
            t1 = datetime.datetime.strptime(str(login_time), "%H:%M:%S")
            t2 = datetime.datetime.strptime(str(logout_time), "%H:%M:%S")
            delta = t2 - t1
            total_working_hours = delta-difference
            print("total_working_hours   ",total_working_hours,difference)
            print("delta",delta)

        # if break_time1 and break_time2:
        #
        #     b1= datetime.datetime.strptime(str(break_time1), "%H:%M:%S")
        #     b2= datetime.datetime.strptime(str(break_time2), "%H:%M:%S")
        #
        #     time_zero =datetime.datetime.strptime('00:00:00', '%H:%M:%S')
        #     breaktime=(b1 - time_zero + b2).time()
        #     print(breaktime,"<<<???")
        #     print((b1 - time_zero + b2).time(),"breaktime")
        # #
        #     total_working_hours= delta- breaktime
        break_durations= []
        # print(d,">>>>>>>>>>>>s")
        # for i in d:
        #
        #     break_durations.append( datetime.datetime.strptime(str(i), "%H:%M:%S") -  datetime.datetime.strptime(str(d[i]), "%H:%M:%S"))
        #     Sum=sum(break_durations)
        # print(Sum,"[]][][[][][]][][][][]")


        Emp_work_hours[names] = total_working_hours

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
