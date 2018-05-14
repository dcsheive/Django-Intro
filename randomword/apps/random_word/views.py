from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
def index(request):
    if 'count' not in request.session:
        request.session['count']= 0
    context = {
        "time": strftime("%B %d, %Y %H:%M %p", gmtime())
    }
    return render(request,'random_word/index.html', context)

def generate(request):
    request.session['word']= get_random_string(length=14)
    request.session['count']+=1
    return redirect('/random_word')

def reset(request):
    request.session.clear()
    return redirect('/random_word')