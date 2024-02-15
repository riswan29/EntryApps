from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserProfile

from django.contrib.auth import authenticate, login

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Buat UserProfile baru dan simpan dengan peran yang sesuai
            user_profile = UserProfile.objects.create(user=user, role=form.cleaned_data['role'])
            return redirect('home')  # Ganti 'home' dengan nama rute yang sesuai
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.userprofile.role == 'entry':
                return redirect('entry_home')
            elif user.userprofile.role == 'keuangan':
                return redirect('keuangan_home')
            elif user.userpofile.role == 'perbaikan':
                return redirect('keuangan_home')
            elif user.userprofile.role == 'dapal':
                return redirect('dapal_home')
            else:
                return redirect('login')
    return render(request,'login.html')

def entry_dash(request):
    return render(request, 'entry.html')
