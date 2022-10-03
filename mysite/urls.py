"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from register import views as v
#views as v because we might import more views, then we need
# to differentiate. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    # this is how we include a different "app's (register)" view
    path('', include("main.urls")),
    #If we dont type anything for our path, it will automatically
    #direct us into main.urls.py
    path('', include("django.contrib.auth.urls")),
    #Sites already made in Django, we just link to them
    # It will go to this application (.auth.urls) and then look in 
    # the url file there, and we will see if we have a valid url
    #  (login, logout etc.)

    
]
