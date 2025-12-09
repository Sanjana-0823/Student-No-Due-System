from os import name
from django import forms
from stnodueapp.models import student,faculty,hallticket,tc,librarydb,sportsdb,contactus, tc_db


class studentform(forms.ModelForm):
    class Meta:
        model= student
        fields=['regno','name','gender','email','course','year','pass1','pass2']


     
class contactform(forms.ModelForm):
    class Meta:
        model= contactus
        fields="__all__"

        
class facultyform(forms.ModelForm):
    class Meta:
        model= faculty
        fields="__all__"    
class hallform(forms.ModelForm):
    class Meta:
        model=hallticket
        fields="__all__"         
class tcform(forms.ModelForm):
    class Meta:
        model=tc_db
        fields="__all__"
         


class libform(forms.ModelForm):
    class Meta:
        model=librarydb
        fields="__all__"         
class spform(forms.ModelForm):
    class Meta:
        model=sportsdb
        fields="__all__"  