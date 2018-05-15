from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request,'survey/index.html')

def process(request):
    if request.method == "POST":
        word = request.POST['thename']
        color = request.POST['sel1']
        if 'comment' not in request.POST:
            size = ''
        else: 
            size = request.POST['comment']
        temp_list = request.session['words']
        temp_list.insert(0,{"word": word, "color": color, "size": size})
        request.session['words'] = temp_list
        print(request.session['words'])
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')