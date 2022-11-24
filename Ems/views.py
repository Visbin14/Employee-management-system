from django.contrib.auth import authenticate, login, logout
from Employee_Management_System import settings
from scrape import break_login_logout
from Ems.models import *
from Ems.Log import logged
from skpy import *
from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import datetime
from django.views.generic.edit import UpdateView
from .models import Employee,Log_status
   

sk = Skype(settings.SKYPE_EMAIL, settings.SKYPE_PASS)

def home(request):
    log_time = break_login_logout()
    def log():
        for i in log_time:  
            if request.POST.get('Break') and request.POST.get('Login') and request.POST.get('Back_to_work') and request.POST.get('logout'):
                if i.content.lower() == logged.get('Break'):
                    a = str(i)
                    b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                    date = a.split("Time")[1].split()[1:2]
                    time= str(a.split("Time")[1].split()[2:3])
                    time=time [2:10]
                    contact = sk.contacts[b]
                    name = contact.name
                    obj = Employee.objects.get(name = name)
                    log = Log_status.objects.create(Emp = obj, Log = "break", Time=time)
                    log.save()
                    logged_time = Logged_Time.objects.create(Employee=obj, Date=date[0])
                    logged_time.Log.add(log)  
                
                
                if i.content.lower().replace(" ","") == logged.get('Login'):
                    a = str(i)
                    b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                    date = a.split("Time")[1].split()[1:2]
                    time= str(a.split("Time")[1].split()[2:3])
                    time=time [2:10]
                    contact = sk.contacts[b]
                    name = contact.name
                    obj1 = Employee.objects.get(name = name)
                    
                    
                    log = Log_status.objects.create(Emp = obj1, Log = "login", Time=time)
                    log.save()
                        
                    logged_time = Logged_Time.objects.create(Employee=obj1, Date=date[0])
                    logged_time.Log.add(log)
                    
            
                if i.content.lower().replace(" ","") == logged.get('Back_to_work'):
                    a = str(i)
                    b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                    date = a.split("Time")[1].split()[1:2]
                    time= str(a.split("Time")[1].split()[2:3])
                    time=time [2:10]
                    contact = sk.contacts[b]
                    name = contact.name
                    obj2 = Employee.objects.get(name = name)
                    
                    
                    log = Log_status.objects.create(Emp = obj2, Log = "back to work", Time=time)
                    log.save()
                        
                    logged_time = Logged_Time.objects.create(Employee=obj2, Date=date[0])
                    logged_time.Log.add(log)
                        
            
                if logged.get('Logout') in i.content.lower():
                    a = str(i)
                    b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                    date = a.split("Time")[1].split()[1:2]
                    time= str(a.split("Time")[1].split()[2:3])
                    time=time [2:10]
                    contact = sk.contacts[b]
                    name = contact.name
                    obj3 = Employee.objects.get(name = name)
                    
                    log = Log_status.objects.create(Emp = obj3, Log = "logout", Time=time)
                    log.save()
                    logged_time = Logged_Time.objects.create(Employee=obj3, Date=date[0])
                    logged_time.Log.add(log)
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
            status = user.check_password(password)
            if status:
                login(request, user)

                return redirect('/')
            else:

                return render(request, 'log/login.html', {'message': "Password  incorrect"})
        except:
            message = "Please check username"
            return render(request, 'log/login.html', {'message': message})

# @login_required(login_url='/login/')
def index(request):
    date1111=request.GET.get('date')
    Emp_work_hours={}
    emp_obj = Employee.objects.all()
    li= []
    b1=[]
    b2=[]
    for emp in emp_obj:
        # x = datetime.datetime(2022, 11, 16)
        login_obj=Logged_Time.objects.filter(Employee=emp,Date=date1111)
        login_time= None
        logout_time= None
        logout_break_time = None
        logout_back_to_work = None
        br = []
        bk = []
        total_break = 0
        for i in login_obj:
            for j in i.Log.all():
                if j.Log == "login":
                    login_time = j.Time

                if j.Log == "logout":
                    logout_time = j.Time

                if j.Log == "break":
                    br.append(j.Time)

                if j.Log=="back to work":
                    bk.append(j.Time)

        br_new = sorted(br)
        bk_new = sorted(bk)
        for br in br_new:
            br_string = br .strftime("%H:%M:%S")
            bt_index = br_new.index(br)
            try:
                bk_string=bk_new[bt_index].strftime("%H:%M:%S")
                b1 = datetime.datetime.strptime(br_string, "%H:%M:%S")
                b2 = datetime.datetime.strptime(bk_string, "%H:%M:%S")
                difference = b2 - b1
                wh = difference.total_seconds()/60/60
                total_break = total_break + wh
            except Exception as e:
                Emp_work_hours[emp.name] = ["total_working_hours", emp.id]
                # continue
        if login_time and logout_time:
            total_working_hours=''
            try:
                t1 = datetime.datetime.strptime(str(login_time), "%H:%M:%S")
                t2 = datetime.datetime.strptime(str(logout_time), "%H:%M:%S")
                delta = t2 - t1
                timet = total_break
                result = datetime.timedelta(hours=timet)
                total_working_hours = str(delta-result)
                hours, minutes,seconds = total_working_hours.split(":")
                c='{} hours, {} minutes'.format(hours,minutes)
                total_working_hours = c

                Emp_work_hours[emp.name] = [total_working_hours, emp.id]
            except:
                print("not found")

    # print("Emp_work_hours",Emp_work_hours)
    return render(request, 'log/index.html', {'data': Emp_work_hours.items()})

# @login_required(login_url='/')
def employee(request):
    a = Employee.objects.all()
    return render(request, 'log/index2.html', {'a': a})


def delete(request, id):
    b = Employee.objects.get(id=id)
    b.delete()
    return redirect('/employee/')

# @method_decorator(login_required, name='dispatch')
class add(View):
    def get(self, request):
        return render(request, 'log/add2.html')

    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        project = request.POST.get('project')
        salary = request.POST.get('salary')
        employee = Employee.objects.create(employee_id=id,name=name,email=email,designation=designation,project=project,salary=salary)
        employee.save()
        return redirect('/employee/')

def logout_view(request):
    if request.user:
        logout(request)
        return redirect('/login/')
# @method_decorator(login_required, name='dispatch')
class APPUpdateView(View):
    def get(self,request,id):
        a = Employee.objects.get(id=id)
        log_object= Logged_Time.objects.filter(Employee=a)
        log_time = None
        out_time = None
        log_break_time = None
        out_back_to_work = None
        mr = []
        mk = []
        mr_new = []
        mk_new = []
        break_times = {}
        # br_list=[b1,b2,b3,b4]
        for n in log_object:
            for p in n.Log.all():
                if p.Log == "login":
                    log_time = p.Time
                if p.Log == "logout":
                    out_time=p.Time
                if p.Log == "break":
                    mr.append(p.Time)
                if p.Log == "back to work":
                    mk.append(p.Time)
                # c +=1
       
        mr_new = sorted(mr)
        mk_new = sorted(mk)
       
        count = 1
        for mr in mr_new:
            full_break = 0
            mr_string = mr .strftime("%H:%M:%S")
            mt_index = mr_new.index(mr)
            try:
                mk_string=mk_new[mt_index].strftime("%H:%M:%S")
                z1 = datetime.datetime.strptime(mr_string, "%H:%M:%S")
                z2 = datetime.datetime.strptime(mk_string, "%H:%M:%S")
                z3=z1.strftime('%H:%M')
                z4=z2.strftime('%H:%M')
                break_times[f"break{count}"] = z3
                break_times[f"back_to_work{count}"] = z4
                count += 1
                break_times.append(z3)
                break_times.append(z4)
                difference = z2 - z1
                mr_string = mr.strftime("%H:%M:%S")
                # m3_index = mr_new.index[1]
                # m4_string = mk_new[m3_index].strftime("%H:%M:%S")
            except:
                pass
        return render(request, 'log/edit.html', {'a': a, 'log_time': log_time, 'out_time': out_time, 'x': break_times})
    def post(self,request,id):
        # date1111=request.GET.get('date')
        b = Employee.objects.get(pk=id)
        print("bbbbbbb",b.id)
        time_obj = Logged_Time.objects.filter(Employee=b)
        logged_time = None
        logout_timee = None
        break_timee = None
        out_back_to_workk = None

        # break_timee=[request.POST.get('break1'), request.POST.get('break2')]
        # out_back_to_workk = [request.POST.get('Back_to_work'),request.POST.get('Back_to_work')]
        back_work_new=[]
        c = 0
        for s in time_obj:
            for q in s.Log.all():
                if q.Log == "login":
                   q.Time = request.POST['login']
                   print(q.Time,"tymmmmmmmmmmmmmmmmmmmmmmmmm")
                if q.Log == "logout":
                    q.Time = request.POST['logout']

                if q.Log == "break":
                    # break_timee.append(q.Time)
                    q.Time = break_timee[c]
                    # q.Time = request.POST['login']
                if q.Log == "back to work":
                    q.Time = out_back_to_workk[c]
                c += 1
                q.Time.save()
        #
        return redirect('/employee/')



# class APPUpdateView(UpdateView):
# 	model = Log_status

# 	fields = [
# 		"log_time",
# 		"out_time"
# 	]
# 	success_url ="/employee/"


















    #     a = Log_status.objects.get(id=id)
    #     a.name = request.POST.get('name')
    #     a.login = request.POST.get('login')
    #     a.break1 = request.POST.get('break1')
    #     a.Back_to_work = request.POST.get('Back_to_work')
    #     a.break2 = request.POST.get('break2')
    #     a.Back__to__work = request.POST.get('Back__to__work')
    #     a.logout = request.POST.get('logout')
    #     all_details= Log_status.objects.create(name=a.name,login=a.login,break=a.break1,back_to_work=a.Back_to_work,break=a.break2)








# class ModelForm(View):
#     def get(self,request,id):
#         a = Employee.objects.get(id=id)
#         print(a,'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>aa')
#         form=ArticleForm(instance=a)
#
#         return render(request,'log/update1.html',{'form':form})
#     def post(self,request,id):
#         form=ArticleForm(request.POST or None)
#         if form.is_valid():
#             print('here')
#             return redirect('/')
#         else:
#             print('here11')
#             pass