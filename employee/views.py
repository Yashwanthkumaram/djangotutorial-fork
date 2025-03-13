from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee ,Contact ,Department ,Location
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
import base64


def respond (request):
    return  HttpResponse("hello world")


# def resp (request ,element_id ):
#         try:
#             return HttpResponse( Employee.objects.get(id=element_id))
#         except ObjectDoesNotExist as E:
#             return  HttpResponse(f"employee with this {element_id} is not present {E}",404 )

             
#         print(Employee.objects.filter(id=element_id).values('ename'))
#         return HttpResponse( Employee.objects.filter(id=element_id).values('ename')[0]['ename'])

def resp (request ,element_id ):
    try:
        employee_obj = Employee.objects.get(id=element_id)
        department_obj = Department.objects.get(id=employee_obj.dept_id_id)
        location_obj = Location.objects.get(id=employee_obj.location_id)




    except:
        return  HttpResponse(f"employee with this {element_id} is not present " )
    
    employee ={
        'name' : employee_obj.ename,
        'id': employee_obj.eid,
        'Designation': employee_obj.designation,
        'deparment': department_obj.dept_name,
        'image' :  base64.b64encode(employee_obj.image).decode('utf-8'),
        'location' : location_obj.loc_name,
        'date' : employee_obj.date_of_joining,
        'email':employee_obj.email


    }

    context ={
        'employee' : employee
    }
    
    return render(request, "emp_details.html", context)
      

from django.http import HttpResponse


def index(request):
    options = Employee.objects.all()
    id = 0

    if request.GET.get('id', 'default') =='default':
        employee_list = Employee.objects.all().order_by('id')
    if request.GET.get('id', 'default') !='default':
        id = request.GET.get('id', 'default')
        employee_list = [Employee.objects.get(id= int(id))]

    template = loader.get_template("index.html")
    context = {
        "employee_list": employee_list , "options":options ,'id':int(id)
    }
    return render(request, "index.html", context)
    
def query1(request):
    #Eid => contact nos 
    employee_list = Employee.objects.get(id=2)
    contact = []
    contact = Contact.objects.filter(employee_id = employee_list.id).values('number')
    context = {
        "employee_list": employee_list ,
    }
    return HttpResponse (contact)

def query2(request):
    #contact no => Emp Details
    contact = Contact.objects.get(number=7678895)
    employee = Employee.objects.filter(id = contact.employee_id_id)
    return HttpResponse (employee)

#----------------------------------------------------------------------------------

from .models import Employee
from rest_framework import viewsets

from .serializers import  EmployeeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#-----------------------------------------

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.decorators import action

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        # department = Department.objects.get(id=pk)
        employees = Employee.objects.filter(dept_id=pk)
        serializer = EmployeeSerializer(employees, many=True)
        # return Response(employees)

        return Response(serializer.data)
       
