from django.shortcuts import render

from scrape import break_login_logout
from skpy import *
from Ems.models import *
sk = Skype("visbinrojer@codesvera.com", "v@visbin@code@pass")

def home(request):

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



    log_time = break_login_logout()
    def break_time():
        lis = []
        for i in log_time:
            lis.append(i)

        
            if i.content.lower() == "break":
                print("\n",i)
       
    
    def back_to_work():
        lis = []
        for i in log_time:
            lis.append(i)

        
            if i.content.lower().replace(" ","") == "backtowork":
                print("\n",i)
       
    

    def login():
        lis = []
        for i in log_time:
            lis.append(i)

        
            if i.content.lower().replace(" ","") == "goodmorning":
                print("\n",i)
    

    def logout():
        lis = []
        for i in log_time:
            lis.append(i)

        
            if "what did you do today" in i.content.lower():
                print("\n",i)

    break_time()
    back_to_work()
    login()    
    logout()
    return render(request,"home.html")




