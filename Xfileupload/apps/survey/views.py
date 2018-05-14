from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage



# Imaginary function to handle an uploaded file.
def index(request):
    return render(request, 'survey/upload.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'survey/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'survey/upload.html')