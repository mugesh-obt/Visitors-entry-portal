from django.shortcuts import render, redirect
from shopify.form import RegisterForm
from shopify.models import Data
from django.contrib import messages
from django.http import HttpResponse


def home(request):
    myform = RegisterForm()
    mydata = Data.objects.all()
    if mydata != '':
        return render(request, 'index.html', {'form': myform, 'datas': mydata})
    else:
        return render(request, 'index.html', {'form': 'myform'})


def addData(request):
    if request.method == 'POST':
        myform = RegisterForm(request.POST)
        if myform.is_valid():
            myform.save()
            messages.success(request, "record added successfully")
            return redirect('homepage')


def updateData(request, id):
    mydata = Data.objects.get(id=id)
    myform = RegisterForm(instance=mydata)
    if request.method == 'POST':
        myform = RegisterForm(request.POST, instance=mydata)
        if myform.is_valid():
            myform.save()
            messages.success(request, "record updated successfully")
            return redirect('homepage')
    context = {'forms': myform}
    return render(request, "update.html", context)


def deleteData(request, id):
    mydata = Data.objects.get(id=id)
    mydata.delete()
    messages.success(request, "record deleted successfully")
    return redirect('homepage')


