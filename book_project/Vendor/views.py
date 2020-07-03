from django.shortcuts import render, redirect
from  Vendor.forms import *

# Create your views here.
def getHome(request):
    return render(request,"index.html")

def book_create(request):
    form=BookCreator()
    template_name='book_create.html'
    context={}
    context["form"]=form
    if request.method=='POST':
        form=BookCreator(request.POST)
        if form.is_valid():
            form.save()
    return render(request,template_name,context)
def add_author(request):
    form=AuthorCreator()
    template_name='add_author.html'
    context={}
    context["form"]=form
    if request.method=='POST':
        form=AuthorCreator(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addauthor")
        else:
            form=AuthorCreator(request.POST)
            context={}
            context["form"]=form
    return render(request,template_name,context)

def add_category(request):
    form=CategoryCreator()
    template_name='add_category.html'
    context={}
    context["form"]=form
    if request.method=='POST':
        form=CategoryCreator(request.POST)
        if form.is_valid():
            form.save()

    return render(request,template_name,context)

def list_books(request):
    template_name='list_book.html'
    qs=Book.objects.all()
    context={}
    context["queryset"]=qs
    return render(request,template_name,context)

def viewBook(request,pk):
    # pk-primary key
    template_name='view_book.html'
    qs=Book.objects.get(id=pk)
    context={}
    context["book"]=qs
    return render(request,template_name,context)

def deleteBook(request,pk):
    template_name='list_book.html'
    qs=Book.objects.get(id=pk).delete()
    context={}
    context["book"]=qs
    # return HttpResponse('deleted')
    return render(request,template_name,context)
def listAuthor(request):
    template_name = 'list_author.html'
    qs = Author.objects.all()
    context = {}
    context["queryset"] = qs
    return render(request, template_name, context)

def deleteAuthor(request,pk):
    template_name='list_author.html'
    qs=Author.objects.get(id=pk).delete()
    context={}
    context["books"]=qs
    return render(request,template_name,context)

def updateBook(request,pk):
    qs=Book.objects.get(id=pk)
    form=BookCreator(instance=qs)
    template_name='update_book.html'
    context={}
    context["form"]=form
    if request.method=='POST':
        form=UpdateBook(request.POST)
        if form.is_valid():
            bname=form.cleaned_data["book_name"]
            categoryname=form.cleaned_data["category_name"]
            authorname=form.cleaned_data["author_name"]
            price=form.cleaned_data["price"]
            page=form.cleaned_data["pages"]
            date=form.cleaned_data["pub_date"]
            qs.book_name=bname
            qs.category_name=categoryname
            qs.author_name=authorname
            qs.price=price
            qs.pages=page
            qs.pub_date=date
            qs.save()
            # form.save()
            return redirect('listbooks')

    return render(request,template_name,context)

def updateAuthor(request,pk):
    qs=Author.objects.get(id=pk)
    form=AuthorCreator(instance=qs)
    template_name='update_author.html'
    context={}
    context["form"]=form
    if(request.method)=='POST':
        form=UpdateAuthor(request.POST)
        if form.is_valid():
            author=form.cleaned_data["author_name"]
            qs.author_name=author
            qs.save()
        return redirect("listauthor")
    return render(request,template_name,context)

def listCategory(request):
    template_name = 'list_category.html'
    qs = Category.objects.all()
    context = {}
    context["queryset"] = qs
    return render(request, template_name, context)

def deleteCategory(request,pk):
    template_name='list_category.html'
    qs=Category.objects.get(id=pk).delete()
    context={}
    context["books"]=qs
    return render(request,template_name,context)

def updateCategory(request,pk):
    qs=Category.objects.get(id=pk)
    form=CategoryCreator(instance=qs)
    template_name='update_category.html'
    context={}
    context["form"]=form
    if(request.method)=='POST':
        form=UpdateCategory(request.POST)
        if form.is_valid():
            category=form.cleaned_data["category_name"]
            qs.category_name=category
            qs.save()
        return redirect("listcategory")
    return render(request,template_name,context)