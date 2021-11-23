from django.shortcuts import render
from django.http import HttpResponse
from .forms import AccountForm

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
    
    return render(request,"register.html",context)
