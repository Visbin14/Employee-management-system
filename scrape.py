from skpy import *

from django.conf import settings

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Employee_Management_System.settings")
django.setup()
# login



def break_login_logout():
    print(">>>>>>>>>>>>>>>>>>")
    sk = Skype(settings.SKYPE_EMAIL, settings.SKYPE_PASS)
    ch = sk.chats["19:1fe0d47033cd4ee692cbd378f28f50f5@thread.skype"]
    get_msg = ch.getMsgs()
    new_list = []
    # for i in get_msg:
    #     new_list.append(i) 
    # return new_list
    for i in range(30):
        # new_list.append(ch.getMsgs()) 
        for j in ch.getMsgs():
            new_list.append(j)
    return new_list 
    # return new_list
    # h = ch.getMsgs()
    # c = ch.getMsgs()
    # a = ch.getMsgs()
    # t = ch.getMsgs()
    # old_list = c + h
    # new_list = a + t
    # combined_list = old_list + new_list

    # lis = []

    # for i in new_list:
    #     lis.append(i)
   
    # print("lis",lis)
    # return lis
