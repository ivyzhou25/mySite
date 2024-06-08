from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from .form import ImageForm
import os

def home(request):
    return render(request, "pages/index.html")

def projects(request):
    return render(request, "pages/projects.html")


def contact(request):
    return render(request, "pages/contact.html")

def product(request):
    if request.method == 'POST':
        #form = ImageForm(request.POST, request.FILES)
        img = request.FILES["file"]
        prompt = request.POST.get('prompt')
        handle_uploaded_file(img)
        
        return render(request, "pages/product_detail.html", {"MEDIA_URL": settings.MEDIA_URL, "img": img})
    else:
        form = ImageForm()
    return render(request, 'pages/product.html', {'form': form})
    
def handle_uploaded_file(f):
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)
        
    file=os.path.join(settings.MEDIA_ROOT, f.name)
    with open(file, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            