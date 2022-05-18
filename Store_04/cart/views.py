from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from customer.models import Account, Customer
from warehouse.models import Book
from store.models import BookItem, LaptopItem, ClothesItem
from .models import Cart, CartBookItem, CartLaptopItem, CartClothesItem
# Create your views here.


def cart_view(request):
    data_auth = request.session['auth']

    items_in_cart = []
    total_cost = 0

    customer_usn = request.session['auth']['username']
    account = Account.objects.get(username=customer_usn)
    customer = Customer.objects.get(account=account)
    cart = Cart.objects.get(customer=customer)

    cart_book_item = CartBookItem.objects.filter(cart=cart)
    cart_laptop_item = CartLaptopItem.objects.filter(cart=cart)
    cart_clothes_item = CartClothesItem.objects.filter(cart=cart)

    # Get item from cart book
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
            'name': book_item.book.title,
            'old_price': book_item.price_in_sale,
            'discount': book_item.discount,
            'new_price': cost,
            'quantity': quantity,
            'product_type': "Books"
        }
        items_in_cart.append(info_item)

    # Get item from cart laptop
    for item in cart_laptop_item:
        laptop_item = item.laptop_item
        quantity = item.quantity
        price = int(laptop_item.price_in_sale)
        discount = int(laptop_item.discount) / 100
        cost = int(price - price * discount) * int(quantity)
        total_cost += cost

        info_item = {
            'id_in_cart': item.id,
            'code': laptop_item.laptop.code,
            'name': laptop_item.laptop.name,
            'old_price': laptop_item.price_in_sale,
            'discount': laptop_item.discount,
            'new_price': cost,
            'quantity': quantity,
            'product_type': "Laptops"
        }
        items_in_cart.append(info_item)

    # Get item from cart clothes
    for item in cart_clothes_item:
        clothes_item = item.clothes_item
        quantity = item.quantity
        price = int(clothes_item.price_in_sale)
        discount = int(clothes_item.discount) / 100
        cost = int(price - price * discount) * int(quantity)
        total_cost += cost

        info_item = {
            'id_in_cart': item.id,
            'code': clothes_item.clothes.code,
            'name': clothes_item.clothes.name,
            'old_price': clothes_item.price_in_sale,
            'discount': clothes_item.discount,
            'new_price': cost,
            'quantity': quantity,
            'product_type': "Clothes"
        }
        items_in_cart.append(info_item)

    return render(request, 'cart/cart_view.html', {'data_auth': data_auth, 'data_cart': items_in_cart, 'total_cost': total_cost})


def cart_add(request):
    if request.POST.get('action') == 'post':
        data = str(request.POST.get('item'))
        product_type, item_id = [x for x in data.split("-")]

        categories = {'Books': BookItem, 'Laptops': LaptopItem, 'Clothes': ClothesItem}
        model = categories[product_type]
        item = model.objects.get(id=item_id)

        quantity = 1

        # Get cart model
        customer_usn = request.session['auth']['username']
        account = Account.objects.get(username=customer_usn)
        customer = Customer.objects.get(account=account)
        cart = Cart.objects.get(customer=customer)

        # Add item to cart database
        if product_type == 'Books':
            cart_book_item = CartBookItem(cart=cart, book_item=item, quantity=quantity)
            cart_book_item.save()
        elif product_type == 'Laptops':
            cart_laptop_item = CartLaptopItem(cart=cart, laptop_item=item, quantity=quantity)
            cart_laptop_item.save()
        elif product_type == 'Clothes':
            cart_clothes_item = CartClothesItem(cart=cart, clothes_item=item, quantity=quantity)
            cart_clothes_item.save()

        # Response to ajax client
        message = "Add to card successfully!"
        data_cart_book_item = CartBookItem.objects.filter(cart=cart)
        data_cart_laptop_item = CartLaptopItem.objects.filter(cart=cart)
        data_cart_clothes_item = CartClothesItem.objects.filter(cart=cart)
        cart_counter = len(data_cart_book_item) + len(data_cart_laptop_item) + len(data_cart_clothes_item)
        response = JsonResponse({'message': message, 'cart_counter': cart_counter})
        return response


def cart_del(request):
    if request.method == 'POST':
        data = request.POST['data']
        product_type, id_item_in_cart = [x for x in data.split("-")]

        categories = {'Books': CartBookItem, 'Laptops': CartLaptopItem, 'Clothes': CartClothesItem}
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
        cart_laptop_item = CartLaptopItem.objects.filter(cart=cart)
        cart_clothes_item = CartClothesItem.objects.filter(cart=cart)
        cart_counter = len(cart_book_item) + len(cart_laptop_item) + len(cart_clothes_item)

        total_cost = 0
        for item in cart_book_item:
            book_item = item.book_item
            quantity = item.quantity
            price = int(book_item.price_in_sale)
            discount = int(book_item.discount) / 100
            cost = int(price - price * discount) * int(quantity)
            total_cost += cost

        for item in cart_laptop_item:
            laptop_item = item.laptop_item
            quantity = item.quantity
            price = int(laptop_item.price_in_sale)
            discount = int(laptop_item.discount) / 100
            cost = int(price - price * discount) * int(quantity)
            total_cost += cost

        for item in cart_clothes_item:
            clothes_item = item.clothes_item
            quantity = item.quantity
            price = int(clothes_item.price_in_sale)
            discount = int(clothes_item.discount) / 100
            cost = int(price - price * discount) * int(quantity)
            total_cost += cost

        # Response to ajax client
        message = "Delete successfully!"
        response = JsonResponse({'message': message, 'cart_counter': cart_counter, 'total_cost': total_cost})
        return response