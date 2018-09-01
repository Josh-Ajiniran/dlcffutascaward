from django import forms
from django.forms import widgets

from .models import Member
from material import *


class RegistrationForm(forms.ModelForm):
    """Form definition for Registration."""
    class Meta:
        """Meta definition for Registrationform."""
        model = Member
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs.update({'class': 'browser-default'})
        self.fields['school'].widget.attrs.update({'class': 'browser-default'})
        self.fields['department'].widget.attrs.update({'class': 'browser-default'})
        self.fields['level'].widget.attrs.update({'class': 'browser-default'})
        self.fields['center'].widget.attrs.update({'class': 'browser-default'})
        self.fields['status'].widget.attrs.update({'class': 'browser-default'})
    
    layout = Layout(
        Fieldset("Personal Info.", 
            Row('surname', 'firstname', 'othername'),
            Row('gender', 'phone_number', 'email'),
            Row('center', 'hall', 'address'),
            Row('status', 'unit')
        ),
        Fieldset("Academics",
            Row('school', 'department', 'level'),
            Row('gpa', 'pgpa'),
            Row('pcgpa', 'ccgpa')
        ),
        Fieldset("100 Level Only",
            Row('mee_score', 'mts_score')
        ),
        Fieldset("PDS Only",
            Row('pds_score')
        )
    )