from django.shortcuts import render
from .forms import StudentRegistraion

# Create your views here.

def showdata(request):
    fm = StudentRegistraion()
    return render(request , 'enrollstudent.html' , {'forms':fm})
