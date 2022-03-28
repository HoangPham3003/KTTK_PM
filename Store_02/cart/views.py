from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from store.models import Category, Book, MobilePhone, Cloth, Laptop, Shoes
from .cart import Cart

# Create your views here.


def cart_view(request):
    categories = {'Books': Book, 'MobilePhones': MobilePhone, 'Clothes': Cloth, 'Laptops': Laptop, 'Shoes': Shoes}
    data = request.session['cart']

    items_in_cart = []
    total_cost = 0
    for x in data:
        category = x['category']
        model = categories[category]
        code = x['code']
        item = get_object_or_404(model, code=code)
        items_in_cart.append(item)
        total_cost += item.price

    return render(request, 'store/cart/cart_view.html', {'data': items_in_cart, 'total_cost': total_cost})


def cart_add(request):
    if request.POST.get('action') == 'post':
        data = str(request.POST.get('item'))
        category, code = [x for x in data.split("-")]

        data_cart = {
            'category': category,
            'code': code
        }

        # Add item to cart in session
        if "cart" not in request.session:
            request.session['cart'] = []

        a = request.session['cart']
        a.append(data_cart)
        request.session['cart'] = a

        # Response to ajax client
        message = "Add to card successfully!"
        cart_counter = len(request.session['cart'])
        response = JsonResponse({'message': message, 'cart_counter': cart_counter})
        return response


def cart_del(request):
    if request.method == 'POST':
        data = request.POST['data']
        category, code = [x for x in data.split("-")]

        item_del = {
            'category': category,
            'code': code
        }

        # Update cart
        data_cart = request.session['cart']
        data_cart.pop(data_cart.index(item_del))
        request.session['cart'] = data_cart

        # Update total cost
        categories = {'Books': Book, 'MobilePhones': MobilePhone, 'Clothes': Cloth, 'Laptops': Laptop, 'Shoes': Shoes}
        total_cost = 0
        for x in data_cart:
            category = x['category']
            model = categories[category]
            code = x['code']
            item = get_object_or_404(model, code=code)
            total_cost += item.price

        # Response to ajax client
        message = "Delete successfully!"
        cart_counter = len(request.session['cart'])
        response = JsonResponse({'message': message, 'cart_counter': cart_counter, 'total_cost': total_cost})
        return response

