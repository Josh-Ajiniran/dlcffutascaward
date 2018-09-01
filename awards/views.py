from django.shortcuts import render, reverse
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.core.files.storage import FileSystemStorage
from django.views import View

from .models import Member
from .forms import RegistrationForm


# TODO: transform function view to class base view

def index(request):
    template = loader.get_template('awards/index.html')
    
    return render(request, 'awards/index.html')

def register_applicant(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reg_success'))
        else:
            print(form.errors.as_data)
    else:
        form = RegistrationForm()

    registered_members_list = Member.objects.order_by('-timestamp')
    template = loader.get_template('awards/registration/registration.html')
    context = {
        'registered_members_list': registered_members_list
    }

    return render(
        request, 'awards/registration/registration.html', 
        {
            'form': form, 
            'registered_members_list': registered_members_list
        },
    )

def register_success(request):
    return render(request, 'awards/registration/success.html')

def qualified_applicants(request):
    # list of qualificatin variables
    best_overall_student = Member.objects.filter(Q(level__exact='200') | Q(level__exact='300')).order_by('-ccgpa').first()
    best_overall_male = Member.objects.filter(Q(gender__exact='M'), Q(level__exact='200') | Q(level__exact='300')).order_by('-ccgpa').first()
    best_overall_female = Member.objects.filter(Q(gender__exact='F'), Q(level__exact='200') | Q(level__exact='300')).order_by('-ccgpa').first()
    best_male_200 = Member.objects.filter(gender__exact='M', level__exact='200').order_by('-ccgpa').first()
    best_female_200 = Member.objects.filter(gender__exact='F', level__exact='200').order_by('-ccgpa').first()  
    best_male_300 = Member.objects.filter(gender__exact='M', level__exact='300').order_by('-ccgpa').first()
    best_female_300 = Member.objects.filter(gender__exact='F', level__exact='300').order_by('-ccgpa').first()
    five_dot_gpa = Member.objects.filter(gpa__exact='5.00').order_by('-timestamp')[:5]  
    
    all_first_class = Member.objects.filter(ccgpa__gte='4.50')
    
    first_35gpa_3rd_class = Member.objects.filter(Q(pcgpa__gte='1.50'), Q(pcgpa__lte='2.39'), Q(pgpa__gte='3.50') | Q(gpa__gte='3.50')).first()
    first_40gpa_2nd_class_lower = Member.objects.filter(Q(pcgpa__gte='2.40'), Q(pcgpa__lte='3.49'), Q(pgpa__gte='4.00') | Q(gpa__gte='4.00')).first()

    best_mee_male = Member.objects.filter(gender__exact='M', level__exact='100').order_by('-mee_score').first()
    best_mee_female = Member.objects.filter(gender__exact='F', level__exact='100').order_by('-mee_score').first()
    best_mts_male = Member.objects.filter(gender__exact='M', level__exact='100').order_by('-mts_score').first()
    best_mts_female = Member.objects.filter(gender__exact='F', level__exact='100').order_by('-mts_score').first()
    best_pds_score = Member.objects.filter(level__exact='PDS').order_by('-pds_score').first()

    template = loader.get_template('admin/members/results.html')
    context = {
        'best_overall_student': best_overall_student,
        'best_overall_male': best_overall_male,
        'best_overall_female': best_overall_female,
        'best_male_200': best_male_200,
        'best_female_200': best_female_200,
        'best_male_300': best_male_300,
        'best_female_300': best_female_300,
        'all_first_class': all_first_class,
        'five_dot_gpa': five_dot_gpa,
        'first_35gpa_3rd_class': first_35gpa_3rd_class,
        'first_40gpa_2nd_class_lower': first_40gpa_2nd_class_lower,
        'best_mee_male': best_mee_male,
        'best_mee_female': best_mee_female,
        'best_mts_male': best_mts_male,
        'best_mts_female': best_mts_female,
        'best_pds_score': best_pds_score,


        'best_overall_student_exp': "Best overall student",
        'best_male_200_exp': "Best overall male result in 200L",
        'best_female_200_exp': "Best overall female result in 200L",
        'best_male_300_exp': "Best overall male result in 300L",
        'best_female_300_exp': "Best overall female result in 300L",
        'best_male_exp': "Overall best male student",
        'best_female_exp': 'Overall best female student',
        'five_dot_gpa_exp': 'A 5.00 GPA',
        'all_first_class_exp': 'Sessional Dean\'s list',
        'first_35gpa_3rd_class_exp': 'First 3.5 GPA of a 3rd class',
        'first_40gpa_2nd_class_lower_exp': 'First 4.0 GPA of a 2nd class lower',
        'best_mee_male_exp': "Best male MEE101 Result",
        'best_mee_female_exp': "Best female MEE101 Result",
        'best_mts_male_exp': "Best male MTS101 Result",
        'best_mts_female_exp': "Best female MTS101 Result",
        'best_pds_score_exp': "Best PDS score",
    }
    
    return HttpResponse(template.render(context, request))

# def print_results(request):
#     html_template = loader.get_template('admin/members/results.html')
#     pdf_file = HTML(html_template).write_pdf
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment;filename="dlcfawards_2018.pdf"'
#     return response


