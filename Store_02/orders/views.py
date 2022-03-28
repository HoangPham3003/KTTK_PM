from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from store.models import Category, Book, MobilePhone, Cloth, Laptop, Shoes
from .models import Order, OrderItem

# Create your views here.


def order_checkout(request):
    categories = {'Books': Book, 'MobilePhones': MobilePhone, 'Clothes': Cloth, 'Laptops': Laptop, 'Shoes': Shoes}

    # Get data cart from session
    data = request.session['cart']

    items_in_cart = []
    total_cost_vnd = 0
    for x in data:
        category = x['category']
        model = categories[category]
        code = x['code']
        item = get_object_or_404(model, code=code)
        items_in_cart.append(item)
        total_cost_vnd += item.price
    total_cost_usd = round(total_cost_vnd/22872, 2)

    # Receive payment request
    if request.method == 'POST':
        # Receive order info
        user_input = dict(request.POST)
        full_name = user_input['fname'][0]
        email = user_input['email'][0]
        address = user_input['address'][0]
        phone = user_input['phone'][0]

        # Save order info in session
        data_order = {
            'full_name': full_name,
            'email': email,
            'address': address,
            'phone': phone
        }
        request.session['data_order'] = data_order

        # Check validation of user input
        if full_name == "" or email == "" or address == "" or phone == "":
            error = "Please enter your information!"
            response = JsonResponse({'error': error})
            return response

        message = "Please pay now!"
        response = JsonResponse({'message': message})
        return response
    return render(request, 'store/order/checkout.html', {'total_cost_vnd': total_cost_vnd, 'total_cost_usd': total_cost_usd})


def success(request):
    categories = {'Books': Book, 'MobilePhones': MobilePhone, 'Clothes': Cloth, 'Laptops': Laptop, 'Shoes': Shoes}

    # Get order info from session
    data_order = request.session['data_order']
    full_name = data_order['full_name']
    email = data_order['email']
    address = data_order['address']
    phone = data_order['phone']


    # Get data cart from session
    data_cart = request.session['cart']

    items_in_cart = []
    total_cost_vnd = 0
    for x in data_cart:
        category = x['category']
        model = categories[category]
        code = x['code']
        item = get_object_or_404(model, code=code)
        items_in_cart.append(item)
        total_cost_vnd += item.price

    # Create a new Order object
    new_order = Order(full_name=full_name, email=email, address=address, phone=phone, total_cost=total_cost_vnd)
    new_order.save()

    for item in items_in_cart:
        item_category = item.category
        item_code = item.code
        item_price = item.price
        # Create a new OrderItem object
        new_order_item = OrderItem(order=new_order, category=item_category, item_code=item_code, price=item_price)
        new_order_item.save()
    message = "Order successfully"
    del request.session['data_order']
    request.session['cart'] = []
    return render(request, 'store/order/success.html', {'message': message})
