from django.contrib import admin

from .models import Member

class MembersInLine(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['surname', 'firstname', 'othername']}),
        ('Personal information', {'fields': ['gender', 'phone_number', 'email', 'address']}),
        ('Church', {'fields': ['center', 'hall', 'status', 'unit']}),
        ('School information', {'fields': ['school', 'department', 'level']}),
        ('Academic information', {'fields': ['pcgpa', 'pgpa', 'gpa', 'ccgpa', 'mee_score', 'mts_score', 'pds_score']})
    ]

    list_display = [
        'surname', 'firstname', 'gender',
        'center', 'hall', 'status', 'unit', 'school', 'department', 'level',
        'pcgpa', 'pgpa', 'gpa', 'ccgpa', 'mee_score', 'mts_score', 'pds_score'
    ]

    list_filter = ['gender', 'center', 'level', 'status', 'ccgpa']
    search_fields = ['surname', 'firstname']

admin.site.register(Member, MembersInLine)