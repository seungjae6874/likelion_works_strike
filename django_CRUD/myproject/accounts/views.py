from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
#구글로그인을 시도해보자
def sociallogin(request):
    return render(request,'sociallogin.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('/')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)


        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': "username or password is incorrect"})
    else:
        return render(request,"login.html")


def signup(request):
    if request.method == "POST":
        #첫번째 비번이랑 두번째 비번이 같으면
        if request.POST["password"] == request.POST["passwordCheck"]:
            try:
                user = User.objects.get(username = request.POST["username"])
                return render(request, 'signup.html', {'error' : "Username has already taken"})
            except:
            #이미 존재하는 아이디가 아니라면 그대로 진행    
                user = User.objects.create_user(
                    username = request.POST["username"],password = request.POST["password"]
                )
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'signup.html', {'error': "Passwors must match"})
    else:
        return render(request, 'signup.html')
    return render(request, 'signup.html')