from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from .models import Emp
from .forms import EmpForm

# Create your views here.

def index(request):
    context ={
        'emps': Emp.objects.all()
    }
    return render(request,'index.html',context)


@login_required(login_url='/')
def create_view(request):
    form = EmpForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        emp = form.save(commit=False)
        emp.author = request.user
        emp.save()
        return HttpResponseRedirect(('/index'))

    return render(request,'create.html',{'form':form})    

def detail_view(request, id):
    try:
        context ={} 
        context["object"] = Emp.objects.get(id = id)
    except ObjectDoesNotExist:  
        return HttpResponse("Error 404: Data not found / User deleted")
    return render(request, "details.html", context)
    
def update_view(request, id):
    instance = get_object_or_404(Emp, id=id)
    form = EmpForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/user/"+str(id))

    context = {
        'form':form
    }

    return render(request,'update.html',context)
    
def delete_view(request, id):
    instance = get_object_or_404(Emp, id=id)
    
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect("/user/"+str(id))
        
    return render(request, 'delete.html', {})