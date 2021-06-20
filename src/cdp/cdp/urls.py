"""cdp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from Blog.views import (
    company_create_view,
    company_detail_view
    
)

from .view import about_us, content, home_page

urlpatterns = [
    path('', home_page),
    path('company-new/', company_create_view),
    path('company/', include('Blog.urls')),
    # path('company/<str:slug>/', company_detail_view),
    # path('company/<str:slug>/edit', company_update_view),
    # path('company/<str:slug>/delete', company_delete_view),
    # path('company/<str:slug>/delete', company_delete_view),



    path('about/', about_us),
    path('content/', content),
    path('admin/', admin.site.urls),
]
