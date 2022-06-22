"""moszabori URL Configuration

The `urlpatterns` list routes URLs to sourceviews. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function sourceviews
    1. Add an import:  from my_app import sourceviews
    2. Add a URL to urlpatterns:  path('', sourceviews.home, name='home')
Class-based sourceviews
    1. Add an import:  from other_app.sourceviews import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('calculator', include('calculator.urls')),


    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
