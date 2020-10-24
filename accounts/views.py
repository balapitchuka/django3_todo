from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        print('in postmethod')
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('/accounts/login/')
        else:
            print('erorros')
            form_errors = signup_form.errors
            return render(request, 'accounts/register.html', {'form_errors' : form_errors})
    else:
        signup_form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form' : signup_form})

