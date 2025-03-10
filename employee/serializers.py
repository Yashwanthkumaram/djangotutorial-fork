from rest_framework import serializers
from .models import Employee ,Contact ,Department ,Location
class EmployeeSerializer(serializers.ModelSerializer):
    profile = Employee()

    class Meta:
        model = Employee
        fields = ['ename', 'email','designation','dept_id','location','image','date_of_joining','salary','experienceex']

  


