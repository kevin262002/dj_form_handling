
from django import forms
 
# creating a form 
class InputForm(forms.Form):
 
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())