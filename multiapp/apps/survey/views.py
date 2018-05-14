from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to display all surveys"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new survey"
    return HttpResponse(response)

