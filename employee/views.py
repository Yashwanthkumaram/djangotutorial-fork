from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee ,Contact
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.core.paginator import Paginator



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
    except:
        return  HttpResponse(f"employee with this {element_id} is not present " )
    
    employee ={
        'name' : employee_obj.ename,
        'id': employee_obj.eid,
        'Designation': employee_obj.designation
    }

    context ={
        'employee' : employee
    }
    
    return render(request, "emp_details.html", context)
      

from django.http import HttpResponse


def index(request):
    employee_list = Employee.objects.all()
    template = loader.get_template("index.html")
    context = {
        "employee_list": employee_list ,
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