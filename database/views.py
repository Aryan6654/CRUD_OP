from django.forms import forms
from database.forms import EmployeeRegistrations
from django.shortcuts import render, HttpResponseRedirect
from .models import User


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        fm = EmployeeRegistrations(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ad = fm.cleaned_data['address']
            reg = User(name=nm, email=em, address=ad)
            reg.save()
            fm = EmployeeRegistrations()
    else:
        fm = EmployeeRegistrations() 
    stud = User.objects.all 

    return render(request, 'createandshow.html', {'form':fm, 'stu':stud})

#This Function Will Update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistrations(request.POST, instance=pi)
        if fm.is_valid:
         fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistrations(instance=pi)
    return render(request, 'editdel.html', {'form':fm})

# This function will delete 
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')