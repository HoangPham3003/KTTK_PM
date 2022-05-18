from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from customer.models import Account, Customer
from warehouse.models import Book
from store.models import BookItem
from .models import Cart, CartBookItem
# Create your views here.


def cart_view(request):
    data_auth = request.session['auth']
    Product_type = "Books"

    items_in_cart = []
    total_cost = 0

    customer_usn = request.session['auth']['username']
    account = Account.objects.get(username=customer_usn)
    customer = Customer.objects.get(account=account)
    cart = Cart.objects.get(customer=customer)
    cart_book_item = CartBookItem.objects.filter(cart=cart)

    for item in cart_book_item:
        book_item = item.book_item
        quantity = item.quantity
        price = int(book_item.price_in_sale)
        discount = int(book_item.discount) / 100
        cost = int(price - price * discount) * int(quantity)
        total_cost += cost

        info_item = {
            'id_in_cart': item.id,
            'code': book_item.book.code,
            'title': book_item.book.title,
            'old_price': book_item.price_in_sale,
            'discount': book_item.discount,
            'new_price': cost,
            'quantity': quantity
        }
        items_in_cart.append(info_item)

    return render(request, 'cart/cart_view.html', {'data_auth': data_auth, 'data_cart': items_in_cart, 'total_cost': total_cost, 'Product_type': Product_type})


def cart_add(request):
    if request.POST.get('action') == 'post':
        data = str(request.POST.get('item'))
        product_type, item_id = [x for x in data.split("-")]

        categories = {'Books': BookItem}
        model = categories[product_type]
        item = model.objects.get(id=item_id)

        quantity = 1

        customer_usn = request.session['auth']['username']
        account = Account.objects.get(username=customer_usn)
        customer = Customer.objects.get(account=account)
        cart = Cart.objects.get(customer=customer)

        # Add item to cart database
        cart_book_item = CartBookItem(cart=cart, book_item=item, quantity=quantity)
        cart_book_item.save()

        # Response to ajax client
        message = "Add to card successfully!"
        data_cart_book_item = CartBookItem.objects.filter(cart=cart)
        cart_counter = len(data_cart_book_item)
        response = JsonResponse({'message': message, 'cart_counter': cart_counter})
        return response


def cart_del(request):
    if request.method == 'POST':
        data = request.POST['data']
        product_type, id_item_in_cart = [x for x in data.split("-")]

        categories = {'Books': CartBookItem}
        model = categories[product_type]

        # Update cart
        cart_item = model.objects.get(id=id_item_in_cart)
        cart_item.delete()

        # Update total cost
        customer_usn = request.session['auth']['username']
        account = Account.objects.get(username=customer_usn)
        customer = Customer.objects.get(account=account)
        cart = Cart.objects.get(customer=customer)
        cart_book_item = CartBookItem.objects.filter(cart=cart)
        cart_counter = len(cart_book_item)

        total_cost = 0
        for item in cart_book_item:
            book_item = item.book_item
            quantity = item.quantity
            price = int(book_item.price_in_sale)
            discount = int(book_item.discount) / 100
            cost = int(price - price * discount) * int(quantity)
            total_cost += cost

        # Response to ajax client
        message = "Delete successfully!"
        response = JsonResponse({'message': message, 'cart_counter': cart_counter, 'total_cost': total_cost})
        return response