# from django.shortcuts import render
# from .models import TodoItem
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import SignUpForm, LoginForm, PasswordChangeCustomForm




# we are passing from here by importing models into todos.html
# def home(request):
#     return HttpResponse("hello vaibhavk")

def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if the user is already logged in
    return redirect('login') 


def signup_view(request):
    if request.method=="POST": #submitted form 
        form=SignUpForm(request.POST)

        if form.is_valid():
            user=form.save() # saves user
            login(request,user) # logs automaticlly 
            return redirect('dashboard') # redirect to dashboard 
     
    else:
        form=SignUpForm() # create a signup form to fill means a get request

    return render(request,'app/signup.html',{'form':form})    

        
def login_view(request):
    if request.method=="POST":
        form=LoginForm(request,data=request.POST) #creates a login form with submitted data

        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    
    else:
        form=LoginForm()

    return render(request,'app/login.html',{'form': form})    


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


# profile page
@login_required

def profile_view(request):
    return render(request,'app/profile.html',{'user':request.user}) # we are passing data to a template


@login_required
def dashboard_view(request):
    return render(request, 'app/dashboard.html', {'user': request.user})



# change password
@login_required

def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Keep the user logged in after password change
            messages.success(request, 'Your password has been updated successfully!')
            return redirect('dashboard')  # Redirect to the dashboard or desired page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeCustomForm(user=request.user)
    return render(request, 'app/change_password.html', {'form': form})

    return render(request,'app/change_password.html',{'form':form})


#forgot password
def forgot_password_view(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)  # Bind user input to the form

        if form.is_valid():  # Check if email exists in the database
            form.save()  # Sends a password reset email (DOES NOT save user data)
            messages.success(request, "Password reset email sent.")
            return redirect('login')  # Redirect to login page after email is sent

    else:
        form = PasswordResetForm()  # Show an empty form when loading the page
    
    return render(request, 'app/forgot_password.html', {'form': form})



