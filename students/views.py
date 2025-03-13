from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.db.models import ExpressionWrapper , Sum ,Count,Avg, FloatField




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
    
#----------------------------------
from rest_framework import viewsets
from .models import Student ,Result, Subject 
from .serializers import StudentSerializer , ResultSerializer ,SubjectSerializer
from rest_framework.response import Response


from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student, Subject, Result
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def studentmarks(self, request, **kwargs):
#         student_id = self.kwargs.get('id') 
#         sem = self.kwargs.get('sem') 

#         student_obj = Student.objects.filter(id=student_id).first()

#         results = Result.objects.filter(student=student_obj, sem=sem)

#         subjects_data = []
#         total_marks = 0

#         for result in results:
#             subjects_data.append({
#                 'subject_id': result.subject.id, 
#                 'subject_name': result.subject.name,
#                 'marks': result.marks
#             })
#             total_marks += result.marks

#         return Response({
#             'id': student_id,
#             'semester': sem,
#             'subjects': subjects_data,
#             'total_marks': total_marks
#         })

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class =SubjectSerializer


