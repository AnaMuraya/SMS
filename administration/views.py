from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import student
import teacher
import employee
import academic

from teacher.models import Department, Designation
from .forms import *

@login_required(login_url='login')
def home_page(request):
    total_student = student.models.AcademicInfo.objects.count()
    total_teacher= teacher.models.PersonalInfo.objects.count()
    total_employee = employee.models.PersonalInfo.objects.count()
    total_class = academic.models.ClassRegistration.objects.count()
    context = {
        'student': total_student,
        'teacher': total_teacher,
        'employee': total_employee,
        'total_class': total_class,
    }
    return render(request, 'administration/home_page.html', context)


def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home_page')
    context = {'forms': forms}
    return render(request, 'administration/login.html', context)

def admin_logout(request):
    logout(request)
    return redirect('home_page')


def add_designation(request):
    forms = AddDesignationForm()
    if request.method == 'POST':
        forms = AddDesignationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('designation')
    designation = Designation.objects.all()
    context = {'forms': forms, 'designation': designation}
    return render(request, 'administration/designation.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been created, you can now login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'administration/register.html', { 'form': form })