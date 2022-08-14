from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # authentication form always takes in request bc it's not creating an instance of a model
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # user = authenticate(request, username=username, password=password)
        # if not user:
        #     context = {
        #         'error': 'invalid username or password'
        #     }
        #     return render(request, 'accounts/login.html', context)
        # print(user)
        # login(request, user)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')
    return render(request, 'accounts/logout.html', {})

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('/login')
    context = { 'form': form }
    return render(request, 'accounts/register.html', context)