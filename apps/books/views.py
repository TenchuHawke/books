from django.shortcuts import render, redirect
from models import Books
from .models import Users
from django.core.urlresolvers import reverse
from datetime import datetime
# Create your views here.

    # TODO move stuff to models
def index(request):
    print "*"*50
    context = {
    "books" : Books.objects.all(),
    }
    print context
    return render(request, 'books/index.html', context)

def addBook(request):
    if request.method == "POST":
        Books.objects.create( bookName=request.POST['Name'], bookDesc=request.POST['Description'], author_id=request.session['user_id'], added_by=Users.objects.get(id=request.session['user_id']))
    return redirect('/books/')

def delete(request, id):
    if request.method == "POST":
        Books.objects.filter(id=id).delete()
    return redirect('/books/')

def edit(request, id):
    if request.method == "POST":
        context = {
        'bId' : id,
        'book' : Books.objects.get(id=id)
        }
        return render(request,'books/edit.html', context)
    return redirect('/books/')

def edit_book(request):
    if request.method == "POST":
        b=Books.objects.get(id=request.POST['id'])
        b.bookName=request.POST['Name']
        if request.POST['Description']:
            b.bookDesc=request.POST['Description']
        b.updated_a=datetime
        b.save()
        # Books.objects.create(id=request.POST['id'], bookName=request.POST['Name'], bookDesc=request.POST['Description']).save()
    return redirect('/books/')
