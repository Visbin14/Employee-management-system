from skpy import *

from Ems.models import Employee,Log_status,Logged_Time

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Employee_Management_System.settings")
django.setup()
#login
sk = Skype("visbinrojer@codesvera.com", "v@visbin@code@pass")


# Break
"""
def breaktime():

    ch = sk.chats["19:1fe0d47033cd4ee692cbd378f28f50f5@thread.skype"]
    c = ch.getMsgs()
    h = ch.getMsgs()
    # a = ch.getMsgs()
    new_list = c+h

    lis = []
    for i in new_list:
        # print("\n",i)
        if i.content.lower() == "break":
            lis.append(i)

    for i in lis:
        print(i)

"""

# login


# def login():
#     ch = sk.chats["19:1fe0d47033cd4ee692cbd378f28f50f5@thread.skype"]
#     c = ch.getMsgs()
#     h = ch.getMsgs()
   

#     new_list = c+h
    

#     lis = []
#     for i in new_list:
        
#         if i.content.lower().replace(" ","") == "goodmorning":
#             lis.append(i)

#     return lis

  
    

# # logout


# def logout():
#     ch = sk.chats["19:1fe0d47033cd4ee692cbd378f28f50f5@thread.skype"]
#     c = ch.getMsgs()
#     h = ch.getMsgs()
#     new_list = c+h
    

#     lis = []
#     for i in new_list:
#         message= i.content
#         if "what did you do today" in message.lower():
#             lis.append(i)

    
#     return lis





def break_login_logout():
    ch = sk.chats["19:1fe0d47033cd4ee692cbd378f28f50f5@thread.skype"]
    c = ch.getMsgs()
    h = ch.getMsgs()
    new_list = c+h

    lis = []
    
    for i in new_list:
        lis.append(i)


    return lis

