from .cart import Cart


def cart(request):
    cart_counter = len(request.session['cart'])
    return {'cart_counter': cart_counter}
