from .models import Cart, CartBookItem
from customer.models import Customer, Account


def cart(request):
    if "auth" in request.session:
        # Get cart
        customer_usn = request.session['auth']['username']
        account = Account.objects.get(username=customer_usn)
        customer = Customer.objects.get(account=account)
        cart = Cart.objects.get(customer=customer)
        cart_book_item = CartBookItem.objects.filter(cart=cart)
        cart_counter = len(cart_book_item)

        # Update total cost in database
        total_cost = 0
        for item in cart_book_item:
            book_item = item.book_item
            quantity = item.quantity
            price = int(book_item.price_in_sale)
            discount = int(book_item.discount) / 100
            cost = int(price - price * discount) * int(quantity)
            total_cost += cost
        cart.total_cost = total_cost
        cart.save()

        return {'cart_counter': cart_counter}
    else:
        return {}

