from django.db import models


SCH_DEPT = (
# SAAT
    ('AEC', 'Agric. Extension & Communication'),
    ('APH', 'Animal Production & Health'),
    ('ARE', 'Agric. Resource Economics'),
    ('CSP', 'Crop, Soil & Pest Mgt.'),
    ('EWM', 'Ecotourism & Wildlife Mgt'),
    ('FST', 'Food Sci. & Tech'),
    ('FWT', 'Forestry & Wood Tech.'),
# SCOM
    ('CSC', 'Computer Sci.'),
    ('CSS', 'Cyber Security'),
    ('IFS', 'Information Sci.'),
    ('IFT', 'Information Tech.'),
    ('SFE', 'Software Engr.'),
# SEET
    ('AGE', 'Agric. & Environ. Engr.'),
    ('CPE', 'Computer Engr.'),
    ('CVE', 'Civil & Environ. Engr.'),
    ('IPE', 'Industrial Prod. Engr.'),
    ('EEE', 'Elect & Electronics Engr.'),
    ('MEE', 'Mechanical Engr.'),
    ('MME', 'Met & Mat Engr.'),
    ('MNE', 'Mining Engr.'),
# SEMS
    ('AGP', 'Applied Geophysics'),
    ('AGY', 'Applied Geology'),
    ('MET', 'Meteorology'),
    ('MST', 'Marine Sci. & Tech.'),
    ('RSG', 'Remote Sensing & Geoinformatics'),
# SET
    ('ARC', 'Architecture'),
    ('BDG', 'Building'),
    ('ESM', 'Estate Management'),
    ('IDD', 'Industrial Design'),
    ('QSV', 'Quantity Surveying'),
    ('SVG', 'Surveying & Geoinformatics.'),
    ('URP', 'Urban & Regional Planning'),
# SHHT
    ('ANA', 'Anatomy'),
    ('BMT', 'Biomedical Technology'),
    ('PHY', 'Physiology'),
# SMAT
    ('ACC', 'Accounting'),
    ('BUS', 'Business Admin'),
    ('ECO', 'Economics'),
    ('EMT', 'Entrepreneurship Mgt. Tech.'),
    ('PMT', 'Project Mgt. Tech.'),
    ('TMT', 'Transport Mgt. Tech.'),
# SOS
    ('BCH', 'Biochemistry'),
    ('BIO', 'Biology'),
    ('CHE', 'Industrial Chemistry'),
    ('MCB', 'Microbiology'),
    ('MTS', 'Mathematical Sci.'),
    ('PHY', 'Physiology'),
    ('STA', 'Statistical Sci.')
)

SCH_LIST = (
    ('SAAT', 'Sch. of Agric. & Agric. Tech.'),
    ('SCOM', 'Sch. of Computing.'),
    ('SEET', 'Sch. of Engr. & Engr. Tech.'),
    ('SEMS', 'Sch. of Earth & Mineral Science.'),
    ('SET', 'Sch. of Environmental Tech.'),
    ('SHHT', 'Sch. of Health & Health Tech.'),
    ('SMAT', 'Sch of Management Tech.'),
    ('SOS', 'Sch. of Science')
)   
LEVEL = (
    ('PDS', 'PDS'),
    ('UABS', 'UABS'),
    ('100', '100'),
    ('200', '200'),
    ('300', '300')
)
GENDER = (('M', 'Male'), ('F', 'Female'))
CENTERS = (
    ('Apatapiti', 'Apatapiti'),
    ('Alejolowo', 'Alejolowo'),
    ('Ibule', 'Ibule'),
    ('Ilara', 'Ilara'),
    ('Footprint', 'Footprint'),
    ('Northgate', 'North Gate')
)
STATUS = (
    ('Leader', 'Leader'),
    ('Worker', 'Worker'),
    ('Member', 'Member')
)

class Member(models.Model):
    surname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    othername = models.CharField(max_length=25, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    phone_number = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=100, verbose_name='Hostel/Lodge Address')
    email = models.EmailField(unique=True)
    school = models.CharField(max_length=50, choices=SCH_LIST)
    department = models.CharField(max_length=50, choices=SCH_DEPT)
    level = models.CharField(max_length=5, choices=LEVEL)
    center = models.CharField(max_length=25, choices=CENTERS)
    hall = models.CharField(max_length=50)
    status = models.CharField(max_length=7, choices=STATUS)
    unit = models.CharField('Unit/Office', max_length=25, blank=True, null=True)
    pcgpa = models.FloatField('Previous CGPA', null=True, blank=True)
    pgpa = models.FloatField('Last Session 2nd Semester GPA', null=True, blank=True)
    gpa = models.FloatField('First Semester GPA', null=True, blank=True)
    ccgpa = models.FloatField('Current CGPA', null=True, blank=True)
    mee_score = models.IntegerField('MEE101 Score', blank=True, null=True)
    mts_score = models.IntegerField('MTS101 Score', blank=True, null=True)
    pds_score = models.IntegerField('PDS Score', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.surname, self.firstname)
