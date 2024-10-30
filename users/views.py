from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            Username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has created been created ,You can login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'users/register.html',{'form':form})


