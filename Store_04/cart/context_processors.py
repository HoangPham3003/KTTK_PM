from .models import Cart, CartBookItem, CartLaptopItem, CartClothesItem
from customer.models import Customer, Account


def cart(request):
    if "auth" in request.session:
        # Get cart
        customer_usn = request.session['auth']['username']
        account = Account.objects.get(username=customer_usn)
        customer = Customer.objects.get(account=account)
        cart = Cart.objects.get(customer=customer)

        cart_book_item = CartBookItem.objects.filter(cart=cart)
        cart_laptop_item = CartLaptopItem.objects.filter(cart=cart)
        cart_clothes_item = CartClothesItem.objects.filter(cart=cart)

        cart_counter = len(cart_book_item) + len(cart_laptop_item) + len(cart_clothes_item)

        # Update total cost in database
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

        cart.total_cost = total_cost
        cart.save()
        return {'cart_counter': cart_counter}
    else:
        return {}

