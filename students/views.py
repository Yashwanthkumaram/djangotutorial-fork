from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student ,Result
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.db.models import ExpressionWrapper , Sum ,Count,Avg, FloatField
from .forms import NameForm


def resp (request ,element_id ):
    try:
        #aggregate Query
        employee_obj = Student.objects.get(id=element_id)
        ans = Student.objects.filter(id=element_id).annotate(sgpa = ExpressionWrapper(Avg('result__marks'),output_field=FloatField())).values('result__sem','sgpa')

    except:
        return  HttpResponse(f"employee with this {element_id} is not present " )
   

    context ={
        'ans' : ans
    } 
    return render(request, "one_student.html", context)
      
from django.http import HttpResponse


def index(request):
    employee_list = Student.objects.all()
    context = {
        "employee_list": employee_list ,
    }
    return render(request, "all_students.html", context)
    

def get_name(request):
    # if this is a POST request we need to process the form data
    ans = None
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            sem = form.cleaned_data["sem"]
            usn = form.cleaned_data["usn"]
            # student = Student.objects.get(usn='USN003')


            try:
                student = Student.objects.get(usn='USN003')
                result = []
                ans = Student.objects.filter(usn=usn).annotate(sgpa = ExpressionWrapper(Avg('result__marks'),output_field=FloatField())).values('result__sem','sgpa')
               


            except:
                return HttpResponse(f"usn and sem combi does not exist{student.usn} ")
             


            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    for res in ans:
                    if res['result__sem'] == sem:
                        result.append(res)
    ans =result
    return render(request, "name.html", {"form": form , "ans":ans})