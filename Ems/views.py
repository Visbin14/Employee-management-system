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
def login(request):
    return render(request, 'log/login.html')

def index(request):
    return render(request, 'log/index.html')

def employee(request):
    return render(request, 'log/index2.html')

def add(request):
    return render(request, 'log/add2.html')






