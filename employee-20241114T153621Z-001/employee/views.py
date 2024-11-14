from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import employee_data
from .forms import EmployeeDataForm

# Create your views here.
def employee_page(request):
    return render(request,"employee/employee_page.html")

class Add_employee(CreateView):
    template_name="employee/add_employee.html"
    model=employee_data
    form_class = EmployeeDataForm
    success_url="/employee"


