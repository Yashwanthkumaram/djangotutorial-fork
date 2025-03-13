from rest_framework import serializers
from .models import Employee,  Department, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


# class DepartmentNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = ['dept']