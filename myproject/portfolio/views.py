from django.shortcuts import render,redirect
from .models import contact
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method=="POST":
        Contact=contact()
        names=request.POST.get('name')
        emails=request.POST.get('email')
        message=request.POST.get('message')
        Contact.name=names
        Contact.email=emails
        Contact.message=message
        Contact.save()
        
        return HttpResponse(" THANKS FOR CONTACT US")
    

    return render(request,"index.html")