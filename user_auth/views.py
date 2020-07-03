from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models  import User
from user_auth.forms import SignUpForm
from Ask.models import *

# Create your views here.

'''def index(request):
    auth = True
    if not request.user.is_authenticated:
        auth = False
    return render(request,'index.html',{'auth':auth,'messages':messages})'''

def sign_up(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        checkbox_data = request.POST 
        if form.is_valid():
            form.save()
            form = form.cleaned_data
            user = User.objects.create_user(**form)
            user.save()
            user  = UserLogin.objects.get(username = form['username'])

            for key,value in checkbox_data.items():
                if(key in ['email','username','password','csrfmiddlewaretoken']):
                    continue
                UserInterest.objects.create(user_id = user,interest_id = Interest.objects.get(pk=int(value)))
                
            messages.success(request,'Your have SignedUp successfully .')
            return redirect('login')
    else:
        form = SignUpForm()
        interests = Interest.objects.all()
    return render(request,'signup.html',{'form':form,'interests':interests})


def login_view(request):

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user  =  authenticate(username=username,password= password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else: 
            messages.error(request,'please check username and password')
            return redirect('login')
    else:
        return render(request,'login.html')

@login_required(redirect_field_name='login')
def change_password(request):
    if request.POST:
        user = request.user
        password = request.POST.get('password',None)
        if password:
            user.set_password(password)
            user.save()
        return redirect('index')
    return render(request,'change_password.html')
        
def logout_view(request):
    logout(request)
    return redirect('index')

