from django import forms

class CreateNewList(forms.Form):
    #Will allow us to have the form automatically generated
    # for us, and other cool stuff;)
    name = forms.CharField(label="Name", max_length=200)
    #We list all our attributes that is included in TodoList.
    check = forms.BooleanField(required=False)