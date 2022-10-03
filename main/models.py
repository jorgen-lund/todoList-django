from django.db import models

# Create your models here.

# Model is a way of modelling information, easier to grab information
# add attributes, edit them, etc. Like java class. 

class TodoList(models.Model):
    # Creating a database object thats called ToDoList.
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        #In case we want to print, this makes it possible
        # This is shown by saving things in terminal f.eks. 
    
class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
