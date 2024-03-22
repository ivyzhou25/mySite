from django.shortcuts import render
from pages.models import Topic
from django.views.decorators.csrf import ensure_csrf_cookie


def home(request):
    return render(request, "pages/index.html")

def projects(request):
    return render(request, "pages/projects.html")


def contact(request):
    return render(request, "pages/contact.html")

def product(request):
    return render(request, "pages/product.html")

def product_detail(request):
    #take input, process it and send result to product_detail.html
    if request.POST:
        product_name = request.POST.get("product_name")
        return render(request, "pages/product_detail.html", {"product": product_name})