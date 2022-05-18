from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import LoginForm
from .models import Customer, Account, Fullname, Address

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usn = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            model = Account
            try:
                data = model.objects.get(username=usn)
                if data.password != pwd:
                    error = "Wrong password!"
                    form = LoginForm()
                    return render(request, 'customer/login.html', {'form': form, 'error': error})
                else:
                    data_auth = {
                        'username': usn
                    }
                    request.session['auth'] = data_auth
                    return redirect('/')
            except:
                error = "Username does not exist!"
                form = LoginForm()
                return render(request, 'customer/login.html', {'form': form, 'error': error})
    else:
        form = LoginForm()
    return render(request, 'customer/login.html', {'form': form})


def logout(request):
    if "auth" in request.session:
        del request.session['auth']
        return redirect('/')


def signup(request):
    return render(request, 'customer/signup.html', {})
