from django.shortcuts import render
from scrape import break_login_logout
from Ems.models import *
from Ems.Log import logged
from skpy import *

sk = Skype("visbinrojer@codesvera.com", "v@visbin@code@pass")

def home(request):

    log_time = break_login_logout()
    def log():
        for i in log_time:
            
            
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











