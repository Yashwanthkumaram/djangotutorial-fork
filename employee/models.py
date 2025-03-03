from django.db import models

class Location(models.Model):
    loc_id = models.CharField(max_length=255, )  
    loc_name = models.CharField(max_length=20)
    loc_state = models.CharField(max_length=255)
    loc_city = models.CharField(max_length=255)
    loc_country = models.CharField(max_length=255)

    def __str__(self):
        return self.loc_name


class Department(models.Model):
    dept_id = models.CharField(max_length=5)  
    dept_name = models.CharField(max_length=20)
    loc_id = models.ForeignKey(Location, on_delete=models.CASCADE)  

    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    eid = models.CharField(max_length=10)  
    ename = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    designation = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2) 
    experience = models.SmallIntegerField()  
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    location = models.ForeignKey(Location, on_delete=models.CASCADE) 
    image = models.BinaryField(null=True)
    date_of_joining = models.DateField(null=True)
 

    def __str__(self):
        return self.ename
    
class Contact(models.Model):
    address = models.CharField(max_length=200)
    number = models.BigIntegerField(max_length=10)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

 