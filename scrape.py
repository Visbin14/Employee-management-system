from skpy import *



import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Employee_Management_System.settings")
django.setup()
#login
sk = Skype("visbinrojer@codesvera.com", "v@visbin@code@pass")


def break_login_logout():
    ch = sk.chats["19:1fe0d47033cd4ee692cbd378f28f50f5@thread.skype"]
    h = ch.getMsgs()
    c = ch.getMsgs()
    a = ch.getMsgs()
    t = ch.getMsgs()
    old_list = c+h
    new_list = a+t
    combined_list = old_list+new_list

    lis = []
    
    for i in combined_list:
        lis.append(i)


    return lis































