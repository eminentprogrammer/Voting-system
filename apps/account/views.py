from distutils.log import Log
from django.shortcuts import render
from . forms import SignupForm, LoginForm



def signup(request):
    form = SignupForm()
    if request.POST:
        
        username = request.POST['username']
        email = request.POST['email']
        fullname = request.POST['fullname']
        password = request.POST['password']

        print(fullname)
    return render(request, "accounts/signup.html", locals())


def login_view(request):
    form = LoginForm()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

    return render(request, "accounts/login.html", locals())