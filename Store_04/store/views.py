from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import BookItem, LaptopItem, ClothesItem, CommentBook, CommentLaptop, CommentClothes
from warehouse.models import Book, Laptop, Clothes
from customer.models import Account, Customer

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
        data_comment = CommentBook.objects.filter(book_item=item_in_sale)
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
        data_comment = CommentLaptop.objects.filter(laptop_item=item_in_sale)
        return render(request, 'store/products/product-detail.html',
                      {'data_auth': data_auth, "Product_type": Ptype, "data_item": data_item, "data_comment": data_comment})
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
        data_comment = CommentClothes.objects.filter(clothes_item=item_in_sale)
        return render(request, 'store/products/product-detail.html',
                      {'data_auth': data_auth, "Product_type": Ptype, "data_item": data_item, "data_comment": data_comment})


def add_comment(request):
    if request.POST.get('action') == 'post':
        data_item = str(request.POST.get('item'))
        data_comment = str(request.POST.get('comment'))
        product_type, item_id = [x for x in data_item.split("-")]

        if data_comment.strip() == "":
            message = "Comment is empty! Please type comment into the text area!"
            response = JsonResponse({'message': message})
            return response
        else:
            # Get item model
            categories = {'Books': BookItem, 'Laptops': LaptopItem, 'Clothes': ClothesItem}
            model = categories[product_type]
            item = model.objects.get(id=item_id)

            # Get customer model
            customer_usn = request.session['auth']['username']
            account = Account.objects.get(username=customer_usn)
            customer = Customer.objects.get(account=account)

            # Add comment into database
            if product_type == "Books":
                new_comment = CommentBook(customer=customer, book_item=item, comment=data_comment)
                new_comment.save()
            elif product_type == "Laptops":
                new_comment = CommentLaptop(customer=customer, laptop_item=item, comment=data_comment)
                new_comment.save()
            elif product_type == "Clothes":
                new_comment = CommentClothes(customer=customer, clothes_item=item, comment=data_comment)
                new_comment.save()

            # Response to ajax client
            message = "Add comment successfully!!!"
            response = JsonResponse({'message': message})
            return response