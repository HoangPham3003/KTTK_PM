from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import BookItem, Comment, LaptopItem, ClothesItem
from warehouse.models import Book, Laptop, Clothes

# Create your views here.


def home(request):
    if "auth" not in request.session:
        return render(request, 'store/home.html', {})
    else:
        data_auth = request.session['auth']
        return render(request, 'store/home.html', {'data_auth': data_auth})


def product_type(request, Ptype):
    categories = {'Books': BookItem, 'Laptops': LaptopItem, 'Clothes': ClothesItem}
    model = categories[Ptype]
    data_products = model.objects.all()

    data_auth = request.session['auth']
    return render(request, 'store/products/product-type.html', {'Product_type': Ptype, 'data_auth': data_auth, 'data_products': data_products})


def product_detail(request, Ptype, id_item):
    data_auth = request.session['auth']

    categories = {'Books': BookItem, 'Laptops': LaptopItem, 'Clothes': ClothesItem}
    model = categories[Ptype]

    item_in_sale = model.objects.get(id=id_item)
    if Ptype == "Books":
        # Get info item
        book_info = Book.objects.get(id=item_in_sale.book.id)

        old_price = int(item_in_sale.price_in_sale)
        discount = int(item_in_sale.discount) / 100
        official_price = int(old_price - old_price * discount)
        data_item = {
            'item_in_sale': item_in_sale,
            'book_info': book_info,
            'official_price': official_price
        }

        # Get comment about item
        data_comment = Comment.objects.filter(book=item_in_sale.id)
        return render(request, 'store/products/product-detail.html', {'data_auth': data_auth, "Product_type": Ptype, "data_item": data_item, "data_comment": data_comment})
    elif Ptype == "Laptops":
        # Get info item
        laptop_info = Laptop.objects.get(id=item_in_sale.laptop.id)

        old_price = int(item_in_sale.price_in_sale)
        discount = int(item_in_sale.discount) / 100
        official_price = int(old_price - old_price * discount)
        data_item = {
            'item_in_sale': item_in_sale,
            'laptop_info': laptop_info,
            'official_price': official_price
        }

        # Get comment about item
        # data_comment = Comment.objects.filter(book=item_in_sale.id)
        return render(request, 'store/products/product-detail.html',
                      {'data_auth': data_auth, "Product_type": Ptype, "data_item": data_item})
    elif Ptype == "Clothes":
        # Get info item
        clothes_info = Clothes.objects.get(id=item_in_sale.clothes.id)

        old_price = int(item_in_sale.price_in_sale)
        discount = int(item_in_sale.discount) / 100
        official_price = int(old_price - old_price * discount)
        data_item = {
            'item_in_sale': item_in_sale,
            'clothes_info': clothes_info,
            'official_price': official_price
        }

        # Get comment about item
        # data_comment = Comment.objects.filter(book=item_in_sale.id)
        return render(request, 'store/products/product-detail.html',
                      {'data_auth': data_auth, "Product_type": Ptype, "data_item": data_item})
