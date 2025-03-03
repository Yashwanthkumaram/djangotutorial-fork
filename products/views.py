from django.shortcuts import render
from django.http import HttpResponse
from .models import Product ,Category
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.db.models import ExpressionWrapper , Sum ,Count,Avg, FloatField
import base64
from django.core.paginator import Paginator


def resp (request ,element_id ):
    try:
        employee_obj = Product.objects.get(id=element_id)
        ans = Product.objects.filter(id=element_id).annotate(sgpa = ExpressionWrapper(Avg('result__marks'),output_field=FloatField())).values('result__sem','sgpa')

    except:
        return  HttpResponse(f"employee with this {element_id} is not present " )
    


    context ={
        'ans' : ans
    }
    
    return render(request, "one_student.html", context)
      

from django.http import HttpResponse


# def index(request):
#     # I couldn't directly do a self join and I will Mobiles dynamically
#     leaf = Category.objects.get(cat_name= 'Mobiles')
#     category_list = Category.objects.all()
#     children_categories = []
#     for category in category_list:
#         if category.cat_id == leaf.pat_id:
#             children_categories.append(category.cat_name)

#     context = {
#         "children_categories": children_categories ,
#     }
#     return render(request, "list_cat.html", context)

    
def index(request):
    # I couldn't directly do a self join and I will Mobiles dynamically
    employee_list = Category.objects.all()
    context = {
        "employee_list": employee_list ,
    }
    return render(request, "cate.html", context)
  


def product (request ,cat_name ):
    try:
        category = Category.objects.get(cat_name = cat_name)
        products = Product.objects.all()
        category_list = Category.objects.filter(pat_id = category.cat_id)
        category_list |= Category.objects.filter(cat_id = category.cat_id)

    except:
        return  HttpResponse(f"No products or Invalid category " )
    img =[]
    result = []
    for product in products:
        for cate in category_list:
            if (product.cat_id_id == cate.cat_id) :
                result.append(product)
                product.image_a = base64.b64encode(product.image).decode('utf-8')



                


    
    paginator = Paginator(result, 1) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    
    context ={
       "result": result , "category_list":category_list ,
       "page_obj":page_obj
    }
    
    return render(request, "product.html", context)
      

from django.http import HttpResponse


def products(request):
    employee_list = Product.objects.all()
    template = loader.get_template("index.html")
    context = {
        "employee_list": employee_list ,
    }
    return render(request, "produts.html", context)

    return HttpResponse( employee_list[0].P_id)



