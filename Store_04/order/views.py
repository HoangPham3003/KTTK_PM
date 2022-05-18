from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from customer.models import Customer, Account, Fullname, Address
from cart.models import Cart, CartBookItem
from .models import Order, OrderItem, Shipment, Payment

# Create your views here.


def order_checkout(request):
    data_auth = request.session['auth']

    customer_usn = request.session['auth']['username']
    account = Account.objects.get(username=customer_usn)
    customer = Customer.objects.get(account=account)

    # Receive payment request
    if request.method == 'POST':
        # Receive order info
        user_input = dict(request.POST)
        full_name = user_input['fname'][0]
        house_number = user_input['house_number'][0]
        street = user_input['street'][0]
        district = user_input['district'][0]
        city = user_input['city'][0]
        country = user_input['country'][0]
        phone = user_input['phone'][0]
        payment = user_input['payment'][0]

        if customer.address.city == "Hà Nội":
            shipment_price = 50000
        else:
            shipment_price = 100000

        cart = Cart.objects.get(customer=customer)
        total_cost_vnd = cart.total_cost + shipment_price
        total_cost_usd = round(total_cost_vnd / 22872, 2)

        # Save order info in session
        data_order = {
            'full_name': full_name,
            'house_number': house_number,
            'street': street,
            'district': district,
            'city': city,
            'country': country,
            'phone': phone,
            'payment': payment,
            'shipment_price': f"{shipment_price}",
            'total_cost_vnd': f"{total_cost_vnd}",
            'total_cost_usd': f"{total_cost_usd}"
        }
        if "data_order" in request.session:
            del request.session['data_order']
        request.session['data_order'] = data_order

        # Check validation of user input
        if full_name == "" or house_number == "" or street == "" or district == "" or city == "" or country == "" or phone == "":
            error = "Please enter your information!"
            response = JsonResponse({'error': error})
            return response

        message = "Check out successfully. Please pay now!"
        response = JsonResponse({'message': message})
        return response
    else:
        data_customer = {
            "full_name": customer.fullname,
            "house_number": customer.address.number_of_house,
            "street": customer.address.street,
            "district": customer.address.district,
            "city": customer.address.city,
            "country": customer.address.country,
            "phone": customer.phone
        }

        if customer.address.city == "Hà Nội":
            shipment_price = 50000
        else:
            shipment_price = 100000

        cart = Cart.objects.get(customer=customer)
        total_cost_vnd = cart.total_cost + shipment_price
        total_cost_usd = round(total_cost_vnd / 22872, 2)

        return render(request, 'order/checkout.html', {'data_auth': data_auth, 'data_customer': data_customer,
                                                       'shipment_price': shipment_price, 'total_cost_vnd': total_cost_vnd,
                                                       'total_cost_usd': total_cost_usd, 'product_cost_vnd': cart.total_cost})


def order_success(request):
    data_auth = request.session['auth']

    # Get order info from session
    data_order = request.session['data_order']
    full_name = data_order['full_name']
    house_number = data_order['house_number']
    street = data_order['street']
    district = data_order['district']
    city = data_order['city']
    country = data_order['country']
    phone = data_order['phone']
    payment = data_order['payment']
    shipment_price = data_order['shipment_price']
    total_cost_vnd = data_order['total_cost_vnd']
    total_cost_usd = data_order['total_cost_usd']

    # Get info customer, cart, cart item
    customer_usn = request.session['auth']['username']
    account = Account.objects.get(username=customer_usn)
    customer = Customer.objects.get(account=account)
    cart = Cart.objects.get(customer=customer)
    cart_book_item = CartBookItem.objects.filter(cart=cart)

    # Create order object
    new_order = Order(customer=customer, cart=cart)
    new_order.save()

    # Create shipment object
    address = f"{house_number}, {street}, {district}, {city}, {country}"
    new_shipment = Shipment(order=new_order, address=address, shipment_price=shipment_price)
    new_shipment.save()

    # Create payment object
    if payment == "Paypal":
        new_payment = Payment(order=new_order, type=payment, total_cost=total_cost_vnd, payment_completed=True)
        new_payment.save()
    else:
        new_payment = Payment(order=new_order, type=payment, total_cost=total_cost_vnd)
        new_payment.save()

    # Create order item object
    for cart_item in cart_book_item:
        product_type = "Books"
        item_id = cart_item.book_item.id
        new_order_item = OrderItem(order=new_order, product_type=product_type, item_id=item_id)
        new_order_item.save()

    # Delete temp data
    del request.session['data_order']
    cart_book_item.delete()

    message = "Order successfully!!!"
    return render(request, 'order/order_success.html', {'data_auth': data_auth, 'message': message})
