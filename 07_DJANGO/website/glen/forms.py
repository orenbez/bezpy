from django import forms
from django.contrib.auth.models import User
from .models import Super, Sub

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
       username = self.cleaned_data.get("username")
       dbuser = User.objects.filter(name=username)

       if not dbuser:
           raise forms.ValidationError("User does not exist in our db!")
       return username


class SuperForm(forms.ModelForm):

    class Meta:
        model = Super
        fields = ['name', 'code']

class Sub(forms.ModelForm):

    class Meta:
        model = Sub
        fields = ['super', 'sub_name']