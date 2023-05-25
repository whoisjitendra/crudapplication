from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    
    
    
    #creating object of model class
    #inserting data into table
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)
    
    
    return redirect('showpage')


def ShowPage(request):
    #select *from tablename
    #for fatching all data of the table
    all_data = Student.objects.all()
    return render(request,'app/show.html',{'key1':all_data})



#Edit page view

def EditPage(request,pk):
    #fatching data of the particular id
    get_data = Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

# update data
def UpdateData(request,pk):
    udata= Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    
    #query to update
    udata.save()
    #render to showpage
    return  redirect('showpage')



#delete data view
def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    #quer for delete
    ddata.delete()
    return  redirect('showpage')    
    
    
    
    
    
    
    
    
    
    
    
    
    