from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'survey/index.html')

def process(request):
    if request.method == "POST":
        request.session['thename'] = request.POST['thename']
        request.session['sel1'] = request.POST['sel1']
        request.session['sel2'] = request.POST['sel2']
        request.session['comment'] = request.POST['comment']
        return redirect('/survey/result')
    else:
        return redirect('/')
def result(request):
    return render(request,'survey/result.html')

def back(request):
    return redirect('/')