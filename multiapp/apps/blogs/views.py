from django.shortcuts import render, HttpResponse, redirect
def index(request):
    response = "Placeholder for list of all blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect("/blogs")

def displayblog(request, number):
    response = "Blog #" + number
    return HttpResponse(response)

def edit(request, number):
    response = "Edit blog #" + number
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/blogs')

