from django import forms
import django_select2

class TestForm(forms.Form):
    CHOICES = (('yes', 'Yes'), ('no', 'No'))
    choice = forms.ChoiceField(choices=CHOICES, widget=django_select2.Select2Widget)
