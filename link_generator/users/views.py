from django.shortcuts import render, redirect
from .form import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Користувач {username} зареєстрований')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request,
                  'users/registration.html',
                  {
                      'title': 'Сторінка реєстрації',
                      'form': form
                  }
                )

@login_required
def profile(request):
    if request.method == 'POST':
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, f'Інформація оновлена')
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)


    data = {
        'updateUserForm': UserUpdateForm,
    }
    return render(request, 'users/profile.html', data)
