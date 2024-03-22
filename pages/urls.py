from django.urls import path
from pages import views


urlpatterns = [
    path("", views.home, name='home'),
    path("projects", views.projects, name="projects"),
    path("contact", views.contact, name="contact"),
    path("product", views.product, name="project"),
    path("product_detail", views.product_detail, name="product_detail")
] 