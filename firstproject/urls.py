"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls), # URL for the admin page
     path('', views.home, name='home'),  # URL for the home page
    path('posts/', views.post_list, name='post_list'), # URL for the post list
    path('post/create/', views.post_create, name='post_create'), # URL for post creation
    path('start/', views.start_page, name='start_page'), # URL for the start page
    path('success/', views.success, name='success'), # URL for the success page

]
