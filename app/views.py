from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import *
import csv
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import JsonResponse


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
    return render(request, 'entry/entry.html')



def export_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="entry_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['NAMA', 'PENDATA', 'NIK', 'TELP', 'TPS', 'KEL', 'KEC', 'KAB'])

    entry_data = EntryData.objects.all()
    for data in entry_data:
        writer.writerow([data.NAMA, data.PENDATA, data.NIK, data.TELP, data.TPS, data.KEL, data.KEC, data.KAB])

    return response

def entry_page(request):
    entry_data_list = EntryData.objects.all()
    paginator = Paginator(entry_data_list, 1000)  # Menentukan 1000 entri per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Hitung nomor urutan yang benar berdasarkan halaman yang sedang aktif
    if page_number:
        current_page_number = int(page_number)
        start_number = (current_page_number - 1) * paginator.per_page + 1
    else:
        start_number = 1

    return render(request, 'entry/master.html', {'page_obj': page_obj, 'start_number': start_number})


def import_data_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)

        for row in csv_reader:
            # Lakukan pengolahan dan simpan data ke database
            EntryData.objects.create(
                NAMA=row['NAMA'],
                PENDATA=row['PENDATA'],
                NIK=row['NIK'],
                TELP=row['TELP'],
                TPS=row['TPS'],
                KEL=row['KEL'],
                KEC=row['KEC'],
                KAB=row['KAB']
            )

        return render(request, 'import_success.html')
    return render(request, 'import_form.html')

def entry_data(request):
    # Mendapatkan opsi kecamatan yang unik dari model EntryData
    kecamatan_options = EntryData.objects.values_list('KEC', flat=True).distinct()

    if request.method == 'POST':
        kecamatan = request.POST.get('kecamatan')
        entries = EntryData.objects.filter(KEC=kecamatan)
        return render(request, 'entry/entry_data_result.html', {'entries': entries, 'kecamatan': kecamatan})

    return render(request, 'entry/entry_data.html', {'kecamatan_options': kecamatan_options})
