from django.db import models



class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=254,unique=True)

    def __str__(self):
        return self.name
    




class Log_status(models.Model):

    log_choices = (
        ("login","login"),
        ("logout","logout"),
        ("break","break"),
        ("back to work","back to work")
    )
    
    Log = models.CharField(max_length=30,choices=log_choices)
    Time = models.TimeField()

    def __str__(self):
        return self.Time
    


class Logged_Time(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date = models.DateField()
    Log = models.ManyToManyField(Log_status)

    def __str__(self):
        return self.Date
    