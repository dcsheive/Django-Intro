from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "blogs/index.html", context)

def test(request):
    response = "Hello, I am test!"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    request.session['name'] = request.POST['name']
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        print("*"*50)
        return redirect("/blogs")
    else:
        return redirect("/blogs")

def displayblog(request, number):
    response = "Blog #" + number
    return HttpResponse(response)

def edit(request, number):
    response = "Edit blog #" + number
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/blogs')

