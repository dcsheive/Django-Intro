from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from random import randint
def index(request):
    if 'gold' not in request.session:
       request.session['gold'] = 0
       request.session['string']=[]
    return render(request,'survey/index.html')

def process(request):
    now = strftime(" %B %d, %Y %H:%M %p", gmtime())
    if request.POST['action'] == 'farm':
        x= randint(10,20)
        request.session['gold'] += x
        request.session['string'].insert(0,['Earned '+str(x)+' gold from the farm!'+now,'green'])
    elif request.POST['action'] == 'cave':
        x= randint(5,10)
        request.session['gold'] += x
        request.session['string'].insert(0,['Earned '+str(x)+' gold from the cave!'+now,'green'])
    elif request.POST['action'] == 'house':
        x= randint(2,5)
        request.session['gold'] += x
        request.session['string'].insert(0,['Earned '+str(x)+' gold from the house!'+now,'green'])
    elif request.POST['action'] == 'casino':
        x= randint(0,50)
        y= randint(0,2)
        if y == 0:
            request.session['gold'] += x
            request.session['string'].insert(0,['Won '+str(x)+' gold at the casino!'+now,'green'])
        else:
            request.session['gold'] -= x
            request.session['string'].insert(0,['Lost '+str(x)+' gold at the casino!'+now,'red'])
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')