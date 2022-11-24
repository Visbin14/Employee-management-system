from django.db import models



class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=254,unique=True)
    designation = models.CharField(max_length=100,null=True, blank=True)
    project = models.CharField(max_length=200,null=True, blank=True)
    salary = models.FloatField(max_length=24,null=True, blank=True)
    def __str__(self):
        return self.name

  
    




class Log_status(models.Model):

    log_choices = (
        ("login","login"),
        ("logout","logout"),
        ("break","break"),
        ("back to work","back to work")
    )
    
    Emp = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    Log = models.CharField(max_length=30,choices=log_choices)
    Time = models.TimeField()



    def __str__(self):
        return f"{self.Log}-{self.Emp}"




    
    


class Logged_Time(models.Model):
    
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date = models.DateField(blank= True,null=True)
    Log = models.ManyToManyField(Log_status,related_name='login_status')

    def __str__(self):
        return f"{str(self.Date) if self.Date else ''}-{self.Employee.name}"
