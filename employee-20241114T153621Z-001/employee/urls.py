from django.urls import  path
from . import views
from .views import Add_employee
urlpatterns = [
    path("", views.employee_page, name='employee_page'),
    path("add_employee", Add_employee.as_view(), name="add_employee")
]
