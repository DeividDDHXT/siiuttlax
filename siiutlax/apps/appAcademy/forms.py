
from django.forms import Form, ModelForms

from .models import Professor, Student

class ProfessorForm(ModelForm):
    model = Professor
    fields = '__all__'

class StudentForm(ModelForm):
    model = Student 
    field = '__all__'

    class Meta:
        model = Professor
        fields = ['username', 'password', 'first_name','numero_trabajador','category']
        widgets = {
            'password': forms.PasswordInput(),
            'numero_trabajador': forms.NumberInput(),
            'category': forms.Select()
        }
    
   
   

    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password', 'first_name' ,'matricula']
        widgets = {
            'password': forms.PasswordInput()
        }