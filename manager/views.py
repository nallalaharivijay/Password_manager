from django.shortcuts import render, redirect
from .forms import PasswordEntryForm
from .models import PasswordEntry

def home(request):
    entries = PasswordEntry.objects.all()
    return render(request, 'manager/home.html', {'entries': entries})

def add_password(request):
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.save_password(form.cleaned_data['password'])
            password_entry.save()
            return redirect('home')
    else:
        form = PasswordEntryForm()
    return render(request, 'manager/add_password.html', {'form': form})

def view_password(request, pk):
    entry = PasswordEntry.objects.get(pk=pk)
    decrypted_password = entry.get_password()
    return render(request, 'manager/view_password.html', {'entry': entry, 'password': decrypted_password})
