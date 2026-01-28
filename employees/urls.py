from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.create_employee, name='employee_add'),
    path('employees/edit/<int:id>/', views.update_employee, name='employee_edit'),
    path('employees/delete/<int:id>/', views.delete_employee, name='employee_delete'),
]
