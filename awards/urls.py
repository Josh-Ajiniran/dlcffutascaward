from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.register_applicant, name='register'),
    path('registration/success/', views.register_success, name='reg_success'),
    path('admin/results/', views.qualified_applicants, name='results'),
    # path('admin/results/print/', views.print_result, name='print_results'),
]