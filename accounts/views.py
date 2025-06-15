from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == 'Doctor':
                return redirect('doctor_dashboard')
            else:
                return redirect('patient_dashboard')
    return render(request, 'login.html')

def doctor_dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user, 'title': 'Doctor Dashboard'})

def patient_dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user, 'title': 'Patient Dashboard'})
