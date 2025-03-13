"""
URL configuration for Mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from employee import views as employee
from students import views as student
from products import views as product

router = routers.DefaultRouter()
router.register(r'users', employee.UserViewSet)
router.register(r'departments', employee.DepartmentViewSet)

router.register(r'students', student.StudentViewSet)
router.register(r'subjects', student.SubjectViewSet)
router.register(r'results', student.ResultViewSet)


router.register(r'products', product.ProductViewSet)
router.register(r'categories', product.CategoryViewSet)
router.register(r'brands', product.BrandViewSet)




urlpatterns = [
    # path("emp/", include("employee.urls")),
    path('', include(router.urls)),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path("students/", include("students.urls")),
    path("categories/", include("products.urls")),



]



