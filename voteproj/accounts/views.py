from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.
# user register view
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, " Account already Registred! " + user)

                return redirect('login')

        context = {'form' : form}
        return render(request, 'register.html', context)


# user login page
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username = email,
                                password = password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Username Or password is incorrect")
                return render(request, 'login.html')

        context = {}
        return render(request, 'login.html', context)

# userlogout page
def logoutpage(request):
    logout(request)
    return redirect('login')