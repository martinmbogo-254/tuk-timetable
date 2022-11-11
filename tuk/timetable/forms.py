from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Timetable



# Create your forms here.

class NewUserForm(ModelForm):
	role_choices=(
		('Lecturer','Lecturer'),
		('Student','Student')
	)
	email = forms.EmailField(required=True)
	role = forms.ChoiceField(choices=role_choices)
	class Meta:
		model = User
		fields = ('email','role')

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
