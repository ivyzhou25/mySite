from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from .form import *
from .openai import process_image, choose_course
import os 

def home(request):
    return render(request, "pages/index.html")

def projects(request):
    return render(request, "pages/projects.html")


def contact(request):
    if request.method == 'POST':
        return render(request, "pages/contact_success.html")
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})

def course(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        response = choose_course(query)
        print(response);
        return render(request, "pages/course_detail.html", {"query": query, "resp" : response})
    else:
        form = CourseForm()
        return render(request, 'pages/course.html', {'form': form})

def product(request):
    if request.method == 'POST':
        #form = ImageForm(request.POST, request.FILES)
        img = request.FILES["file"]
        prompt = request.POST.get('prompt')
        resp = handle_uploaded_file(img, prompt)
        
        return render(request, "pages/product_detail.html", {"MEDIA_URL": settings.MEDIA_URL, "img": img, "resp" : resp})
    else:
        form = ImageForm()
        return render(request, 'pages/product.html', {'form': form})
    
def handle_uploaded_file(f, prompt):
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)
    
    file = os.path.join(settings.MEDIA_ROOT, f.name)
    with open(file, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    response = process_image(file, prompt)
    print (response.json())
    return response.json()['choices'][0]['message']['content']
            