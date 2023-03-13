from django.shortcuts import render
from .forms import StudentRegitaion
from .models import User
from django.http import HttpResponseRedirect

# Create your views here.
def add_show(r):
    if r.method =='POST':
        fm = StudentRegitaion(r.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            #pw = fm.cleaned_data['password']
            reg = User(name =nm,email=em)
            reg.save()
            fm = StudentRegitaion()
    else:
        fm = StudentRegitaion()
    stud = User.objects.all()
    return render(r,'addandshow.html',{'form':fm, 'stu':stud})

def delete_data(r,id):
    #if r.method == "POST":
        pi = User.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(r,id):
    if r.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegitaion(r.POST,instance=pi)
        if fm.is_valid():
            fm.save(commit=True)
            #fm.set_password(fm.password).save()
            return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegitaion(instance=pi)
        #return HttpResponseRedirect('/')
    return render(r,'Updatestudent.html',{'form':fm})
