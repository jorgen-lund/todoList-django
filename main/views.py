from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList

#PART 1
# def index(response):
#     return HttpResponse("<h1>Kjell Fresh!</h1>")

#PART 2

# def index(response, id):
#     return HttpResponse("<h1>%s</h1>" %id)
#     # Dynamic page or something like that. typing /1 in 
#     # web browser shows up 1

#PART 3
# def index(response, id):
#     ls = TodoList.objects.get(id=id)
#     #Is 2 in my case, because I deleted the 1 in the database
#     item = ls.item_set.get(id=1)
#     #Creating the item in python to be equal to the one in the 
#     # database
#     return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))
#     # need to include str around item.text
#     # Also need to wrap all of the last %s in paranthesis()

#Part 4
# def index(response, id):
#     ls = TodoList.objects.get(id=id)
#     return render(response, "main/base.html", {"name":ls.name})
#     # Now rendering the html file.


# def home(response):
#     return render(response, "main/home.html", {"name": "test"})

def index(response, id):
    ls = TodoList.objects.get(id=id)
    # Don't need anything inside the curly brackets 
    # Because that is handled in the html files.
    # However, we kind of want to put our todolist in there.
    # Also changed to main/list as opposed to main/base

    #PART 6
    if response.method == "POST":

        #Saving the check buttons
        print(response.POST)
        if response.POST.get("save"):

            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()
 


        elif response.POST.get("newItem"):
            #Getting the text from the input
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid input")


    return render(response, "main/list.html", {"ls": ls})



def home(response):
    return render(response, "main/home.html", {})

#PART 5 
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        # All the information from our from.
        # When we get this response, we will get a dict
        # of all the values.
        # It creates a new form that has those values in them.

        if form.is_valid():
            # The is_valid method exists because we inherit 
            # from forms.Form in forms.py

            n = form.cleaned_data["name"]
            # cleaned_data unencrypts the data
            # We use "name" because it is a field in our TodoList model
            t = TodoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
        # Will redirect us to the webpage with that TodoList.
        # Dynamic stuff, looked on earlier with the urls.
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})

