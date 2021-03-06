"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import ListView, DetailView
from shop.models import Bikes, Menu

urlpatterns = [
    path('webexample/', include('webexample.urls')),
    path('', ListView.as_view(queryset=Menu.objects.all().order_by("name")[:15], template_name="shop/menu.html")),
    path('<pk>/', DetailView.as_view(model = Menu, template_name = "shop/post.html")), 
]