from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    #When searching for blank webpath, we go to the path 
    #named "index" in the views.py file.
    # Through adding the <int:id> in the path, our index
    # in Views now needs an extra field called "id"

    path("", views.home, name="home"),
    
    #NEW Page to create Todolists and Items
    path("create/", views.create, name="create"), 
]
