from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login,logout,authenticate
from .forms import *
# Create your views here.
def index(request):
	return render(request,'index.html')


def signup(request):

	if request.method =='POST':
		import pdb;pdb.set_trace()
		form = Signupform(request.POST)

		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email','')
			password = form.cleaned_data.get('password','')
			user = authenticate(email = email,password = password)
			return redirect('index')
		else:
			print(form.errors)
			return render(request,'signup.html',{ 'form': form })
	else:
		form = Signupform()
		return render(request,'signup.html',{ 'form': form })


def signin(request):

	if request.method=="POST":
		import pdb;pdb.set_trace()
		form = Signinform(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(email = email, password = password)
			login(request,user)
			return redirect('index')
		else:
			print(form.errors)
			return render(request,'signin.html',{ 'form': form })
	else:
		form = Signinform()
		return render(request,'signin.html',{ 'form': form })



def logout_req(request):
    logout(request)
    return redirect("index")