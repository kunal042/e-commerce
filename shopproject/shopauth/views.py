from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout ,authenticate
from django.contrib import messages




def sign_up(request):
    if request.method == "POST":
        email = request.POST['email']
        
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, "Password is Not macthing")
            return render(request, 'auth/signup.html')



        myuser = User.objects.create(email, password)
        myuser.save()
        messages.info(request, "Signup Sucessfully Please Login")
        return redirect("/auth/login/")
    
    return render(request, 'auth/signup.html')


    

def login(request):

    
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username, userpassword=userpassword)
       
    
        if myuser is not None:
            login(request, myuser)
            messages.success(request,"Login Success")
            return render(request, 'index.html')
        else:
            messages.error(request, "Something Went Wrong")
            return HttpResponse("/auth/login/")
        

    return render(request, 'auth/login.html')
