from django.forms import Form,ModelForm
from .models import Professor,Student
from django import forms


class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ['username', 'password', 'first_name','numero_trabajador']
        widgets = {
            'password': forms.PasswordInput(),
            'numero_trabajador': forms.NumberInput()
        }
    
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password', 'first_name','matricula']
        widgets = {
            'password': forms.PasswordInput()
        }