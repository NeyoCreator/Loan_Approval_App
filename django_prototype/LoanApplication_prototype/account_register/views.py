from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AccountForm, Personal_Detail_form
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from .models  import Account, Personal_Details


# Create your views here.

#Homepage
def home_view(request,*args, **kwargs):
    return render(request, "home.html", {})

#Account register
def register_account(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AccountForm()

    context = {
        "form":form
    }
    obj = Account.objects.get(id=1)
    print(obj)
    return render(request,"register.html",context)

def register_personal_details(request):
    #Process Images Uploaded by user
    if request.method == "POST":
        form = Personal_Detail_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #Get the current instance to diplay in the template
            img_obj = form.instance
            return render(request,'personal_details.html', {'form':form, 'img_obj':img_obj})
            
        else :
            form = Personal_Detail_form()
        return  render(request,"personal_details.html", {'form':form})