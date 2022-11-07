from django.shortcuts import render
from scrape import break_login_logout
from Ems.models import *
from skpy import *

sk = Skype("visbinrojer@codesvera.com", "v@visbin@code@pass")

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
                # print("break:",name,date,time)
                obj = Employee.objects.get(name = name)
                
                if i.content.lower() == "break":
                    log = Log_status.objects.create(Emp = obj, Log = "break", Time=time)
                    log.save()
                    logged_time = Logged_Time.objects.create(Employee=obj, Date=date[0])
                    logged_time.Log.add(log)  
               

              
                


             
            
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
                
                obj1 = Employee.objects.get(name = name)
                
                if i.content.lower().replace(" ","") == "goodmorning":
                    log = Log_status.objects.create(Emp = obj1, Log = "login", Time=time)
                    log.save()
                    
                    logged_time = Logged_Time.objects.create(Employee=obj1, Date=date[0])
                    logged_time.Log.add(log)
                # print("login:",name,date,time)
                
            
            if i.content.lower().replace(" ","") == "backtowork":
                # print("\n","back to work : ", i)
                a = str(i)
                b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                time= str(a.split("Time")[1].split()[2:3])
                time=time [2:10]
                contact = sk.contacts[b]
                name = contact.name
                obj2 = Employee.objects.get(name = name)
                
                if i.content.lower().replace(" ","") == "backtowork":
                    log = Log_status.objects.create(Emp = obj2, Log = "back to work", Time=time)
                    log.save()
                    logged_time = Logged_Time.objects.create(Employee=obj2, Date=date[0])
                    logged_time.Log.add(log)
                
                # print("back to work:",name,date,time)
                
               
            
            
            # lis = []
            if "what did you do today" in i.content.lower():
                # print("\n","logout : ",i)
                a = str(i)
                b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
                date = a.split("Time")[1].split()[1:2]
                time= str(a.split("Time")[1].split()[2:3])
                time=time [2:10]
                contact = sk.contacts[b]
                name = contact.name
                obj3 = Employee.objects.get(name = name)
                
                if "what did you do today" in i.content.lower():
                    log = Log_status.objects.create(Emp = obj3, Log = "logout", Time=time)
                    log.save()
                    logged_time = Logged_Time.objects.create(Employee=obj3, Date=date[0])
                    logged_time.Log.add(log)
                # print("logout:",name,date,time)
                
                        
               
       
    
    log()

         
    
      
    return render(request,"home.html")









    # # login
    
    # Login= login()
    # for i in Login:
      
    #     a= str(i)
    #     b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()

       

    #     date = a.split("Time")[1].split()[1:2]

    #     time= str(a.split("Time")[1].split()[2:3])
    #     time=time [2:10]
        
    #     contact = sk.contacts[b]

       
        
    #     name = contact.name

    #     print(name, date, time)
        
    #     # break
       
 
    # print("-----------------")

    # # logout

    # Logout = logout()
    # for i in Logout:
    #     a = str(i)
    #     b= a.split("UserId")[1].strip()[1:].strip().split("ChatId:")[0].strip()
    #     date = a.split("Time")[1].split()[1:2]

    #     time= str(a.split("Time")[1].split()[2:3])
    #     time=time [2:10]
        
    #     contact = sk.contacts[b]
    #     name = contact.name


    #     print(name,date,time)





