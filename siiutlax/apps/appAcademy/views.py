from django.shortcuts import render

from apps.appAcademy.models import Student

# Create your views here.

from .forms import ProfesorForm, StudentForm


def create_professor(request):
    form = ProfesorForm()
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
            
    return render(request,
                  'academy/create_professor.html',
                  {'form':form})

    
def create_student(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            matricula = form.cleaned_data['matricula']
            
            Student.object.create_user(
                
            username=username,
            first_name=first_name,
            password=password,
            matricula=matricula,
                
            )
    
    form = StudentForm()
    return render(request,
                  'academy/create_student.html',
                  {'form':form})
    
