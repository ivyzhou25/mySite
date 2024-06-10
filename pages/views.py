from django.shortcuts import render
from pages.models import Image
from django.views.decorators.csrf import ensure_csrf_cookie
from .form import ImageForm
from django.conf.urls.static import static
from django.conf import settings
from pages.openai import encode_image, process_image
import os


def home(request):
    return render(request, "pages/index.html")

def projects(request):
    return render(request, "pages/projects.html")


def contact(request):
    return render(request, "pages/contact.html")

def product(request):
    if request.method == 'POST':
        img = request.FILES["file"]
        ## call openai to get image description
        
        resp = handle_uploaded_file(img)
        
        return render(request, "pages/product_detail.html", {"MEDIA_URL": settings.MEDIA_URL, "img": img, "resp" : resp})
    else:
        form = ImageForm()
        return render(request, 'pages/product.html', {'form' : form})

def handle_uploaded_file(f):
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)
    
    file = os.path.join(settings.MEDIA_ROOT, f.name)
    with open(file, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
      
    # encode this image and print(encoded)
    #encode = encode_image(file);
    
    response = process_image(file)
    print (response.json())
    return response.json()['choices'][0]['message']['content']
    
def life(request):
    return render(request, "pages/life.html")