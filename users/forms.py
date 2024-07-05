from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.forms import ModelForm
from django.contrib.auth.models import User 
from .models import Profile , Skills


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name" , "username", "email", "password1", "password2"]
        labels ={
            'first_name':'Full Name'
        }
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})



class update_profile_form(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'email', 'username','headline', 'bio', 'location','profile_image', 'social_github' , 'social_twitter' , 'social_linkedin' , 'social_youtube' , 'social_website']

    
    def __init__(self, *args, **kwargs):
        super(update_profile_form, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class skillform(ModelForm):

    class Meta:
        model = Skills
        fields = "__all__"
        exclude = ["owner"]
        