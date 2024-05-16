from django.shortcuts import render




def sign_up(request):
    return render(request, 'auth/signup.html')

def login(request):
    return render(request, 'auth/login.html')
