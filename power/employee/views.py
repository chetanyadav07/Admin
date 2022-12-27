from django.shortcuts import render , redirect
from .forms import EmpForm
from .models import Employee

# Create your views here.
def add(request):
    empForm = EmpForm()
    return render(request,'add.html',{'empForm': empForm})

def insert(request):
    if request.method=="POST":
        empForm=EmpForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            return render(request, 'show.html')
        else:
            return render(request, 'add.html')    
    return render(request, 'add.html')        
    

def show(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employees':employees})

def edit(request,eid):
    emp=Employee.objects.get(eid=eid)
    return render(request,'edit.html',{'emp':emp})

def update(request,eid):
    if request.method=="POST":
        emp=Employee.objects.get(eid=eid)
        form=EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return render(request,'show.html')
        else:
            return render(request, 'edit.html')
    else:
          return render(request, 'edit.html')

def delete(request,eid):
    emp=Employee.objects.get(eid=eid)
    emp.delete()
    return redirect('show')