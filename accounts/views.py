from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

@login_required
def admin_register_view(request):
    if(request.method == 'POST'):
        user_form = UserCreationForm(request.POST)
        if(user_form.is_valid()):
            user_form.save()
            return redirect('users_list')
        
    else:
        user_form = UserCreationForm()

    return render (
        request,
        'admin_register.html', {
            'user_form': user_form,
            'form_error': user_form.errors
        }
    )

def user_register_view(request):
    if (request.method == 'POST'):
        user_form = UserCreationForm(request.POST)
        if (user_form.is_valid()):
            user_form.save()
            return redirect('home')
    else:
        user_form = UserCreationForm()

    return render(
        request,
        'user_register.html', {
            'user_form': user_form,
            'form_error': user_form.errors
        }
    )


def login_view(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if(user is not None):
            login(request, user)
            return redirect('cars_list')

        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()

    return render (
        request,
        'login.html', {
            'login_form': login_form
        }
    )

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
