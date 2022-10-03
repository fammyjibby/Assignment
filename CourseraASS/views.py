from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already used')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,password=password)
            user.save();
            return redirect('index')
    else:
        return render(request,"register.html")
