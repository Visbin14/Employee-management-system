
import sys,django,os
project_dir_path = os.path.abspath(os.getcwd())
sys.path.append(project_dir_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Employee_Management_System.settings')
django.setup()

logged = {'Break':"break",
       'Login':"goodmorning",
       'Back_to_work':"backtowork",
       'Logout':"what did you do today"
       }
