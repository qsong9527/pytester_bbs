"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views as bbsviews
from pywebdriver import views as pyviews

urlpatterns = [
    # path('$', bbsviews.index),
    path(r'admin/', admin.site.urls),
    path(r'bbs/', bbsviews.index),
    path(r'webdriver/', pyviews.index),
    path(r'webdriver/location', pyviews.location_practices_page),
    path(r'webdriver/element', pyviews.element_practices_page),
    path(r'webdriver/10seconds', pyviews.wait10sec_practices_page),
    path(r'webdriver/frame', pyviews.frame_practices_page),
    path(r'webdriver/frame_content', pyviews.frame_practices_page_frame_content),
    path(r'webdriver/frame_func', pyviews.frame_practices_page_frame_func),
    path(r'webdriver/frame_iframe', pyviews.frame_practices_page_iframe),
]
