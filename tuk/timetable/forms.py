from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Timetable



# Create your forms here.

class NewUserForm(UserCreationForm):
	role_choices=(
		('Lecturer','Lecturer'),
		('Student','Student')
	)
	email = forms.EmailField(required=True)
	role = forms.ChoiceField(choices=role_choices,required=True)
	
	class Meta:
		model = User
		fields = ('username','email','role','password1','password2')

		def save(self, commit=True):
			user = super(NewUserForm, self).save(commit=False)
			user.role = self.cleaned_data["role"]
			if commit:
				user.save()
			return user
		
