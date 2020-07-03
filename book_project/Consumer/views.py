from django.shortcuts import render, redirect
from Consumer.forms import ConsumerRegForm, ConsumerLogin
from Consumer.models import *


# Create your views here.
from Vendor.models import Book


def consumerHome(request):
    template_name='consumer/home.html'
    return render(request,template_name)
def consumerRegistration(request):
    form=ConsumerRegForm()
    template_name='consumer/registration.html'
    context={}
    context["form"]=form
    if request.method=='POST':
        form=ConsumerRegForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("login")
    return render(request,template_name,context)
def consumerLogin(request):
    form=ConsumerLogin()
    template_name="Consumer/login.html"
    context={}
    context["form"]=form
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        qs=Consumer.objects.get(username=username)
        if (qs):
            if (password == qs.password):
                print("ok")
                print("successfully Login")
                return redirect("home")
            else:
                return render("consumer/login.html")

    # if request.method=="POST":
    #     print("inside post")
    #     form=ConsumerLogin(request.POST)
    #     if form.is_valid():
    #
    #         username = form.cleaned_data["username"]
    #         psd = form.cleaned_data["password"]
    #         print(username,psd)
    #         qs=Consumer.objects.get(username=username)
    #
    return render(request,template_name,context)

def home(request):
    return render(request,'consumer/home.html')

def consumerHome(request):
    template_name='consumer/consumer_home.html'
    qs=Book.objects.all()
    context={}
    context["book"]=qs
    return render(request,template_name,context)

def buyNow(request,pk):
    template_name='consumer/buynow.html'
    qs = Book.objects.get(id=pk)
    context = {}
    context["book"] = qs
    return render(request, template_name, context)