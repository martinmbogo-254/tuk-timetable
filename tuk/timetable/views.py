from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewUserForm
# Create your views here.
# one must be logged in inorder to see this page
@login_required(login_url='login')
def home(request):
    return render(request,'timetable/home.html')
# registration view

# login view
def login_request(request):
    if request.method=="POST":
        form =AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {{username}}")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
        context ={
            'login_form': form
        }
        form = AuthenticationForm()
        return render(request=request,template_name='timetable/login.html',context=context)


# register page code view
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Registration failed..please read the instructions and try again..!!!")
	form = NewUserForm()
	return render (request=request, template_name="timetable/register.html", context={"register_form":form})
