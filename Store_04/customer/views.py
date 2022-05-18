from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import LoginForm, SignupFormAccount, SignupFormInformation, ChangePwdForm
from .models import Customer, Account, Fullname, Address
from cart.models import Cart

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
    if request.method == 'POST':
        form_account = SignupFormAccount(request.POST)
        form_info = SignupFormInformation(request.POST)
        if form_account.is_valid() and form_info.is_valid():
            usn = form_account.cleaned_data['username']
            pwd = form_account.cleaned_data['password']
            pwd_retyped = form_account.cleaned_data['password_retyped']

            firstname = form_info.cleaned_data['firstname']
            midname = form_info.cleaned_data['midname']
            lastname = form_info.cleaned_data['lastname']
            house_number = form_info.cleaned_data['house_number']
            street = form_info.cleaned_data['street']
            district = form_info.cleaned_data['district']
            city = form_info.cleaned_data['city']
            country = form_info.cleaned_data['country']
            dob = form_info.cleaned_data['dob']
            phone = form_info.cleaned_data['phone']

            if pwd != pwd_retyped:
                error = "Password retyped must be same with new password!"
                form_account = SignupFormAccount(request.POST)
                form_info = SignupFormInformation(request.POST)
                return render(request, 'customer/signup.html',
                              {'form_account': form_account, 'form_info': form_info, 'error': error})
            else:
                try:
                    data = Account.objects.get(username=usn)
                    error = "Username existed!"
                    form_account = SignupFormAccount(request.POST)
                    form_info = SignupFormInformation(request.POST)
                    return render(request, 'customer/signup.html', {'form_account': form_account, 'form_info': form_info, 'error': error})
                except:
                    new_account = Account(username=usn, password=pwd_retyped)
                    new_account.save()
                    new_address = Address(number_of_house=house_number, street=street, district=district, city=city, country=country)
                    new_address.save()
                    new_fullname = Fullname(firstname=firstname, midname=midname, lastname=lastname)
                    new_fullname.save()
                    new_customer = Customer(dob=dob, phone=phone, account=new_account, address=new_address, fullname=new_fullname)
                    new_customer.save()
                    new_cart = Cart(customer=new_customer, total_cost=0)
                    new_cart.save()
                    return redirect("/customer/login")
    else:
        form_account = SignupFormAccount()
        form_info = SignupFormInformation()
        return render(request, 'customer/signup.html', {'form_account': form_account, 'form_info': form_info})


def change_password(request):
    data_auth = request.session['auth']
    customer_usn = data_auth['username']
    account = Account.objects.get(username=customer_usn)
    old_pwd = account.password

    if request.method == 'POST':
        form = ChangePwdForm(request.POST)
        if form.is_valid():
            old_pwd_inp = form.cleaned_data['old_password'].strip()
            new_pwd_inp = form.cleaned_data['new_password'].strip()
            new_pwd_retyped_inp = form.cleaned_data['new_password_retyped'].strip()

            if old_pwd_inp == "" or new_pwd_inp == "" or new_pwd_retyped_inp == "":
                error = "Please enter information!"
                form = ChangePwdForm()
                return render(request, 'customer/change_password.html', {'data_auth': data_auth, 'form': form, 'error': error})
            elif old_pwd_inp != old_pwd:
                error = "Old password is wrong!"
                form = ChangePwdForm()
                return render(request, 'customer/change_password.html', {'data_auth': data_auth, 'form': form, 'error': error})
            elif new_pwd_inp == old_pwd:
                error = "New password must be different from old password!"
                form = ChangePwdForm()
                return render(request, 'customer/change_password.html', {'data_auth': data_auth, 'form': form, 'error': error})
            elif new_pwd_inp != new_pwd_retyped_inp:
                error = "New password retyped must be same as new password!"
                form = ChangePwdForm()
                return render(request, 'customer/change_password.html', {'data_auth': data_auth, 'form': form, 'error': error})
            else:
                account.password = new_pwd_retyped_inp
                account.save()
                return redirect("/customer/logout")
    else:
        form = ChangePwdForm()
        return render(request, 'customer/change_password.html', {'data_auth': data_auth, 'form': form})


