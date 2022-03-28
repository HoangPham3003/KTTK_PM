from django.shortcuts import render, get_object_or_404
from .models import Category, Book, MobilePhone, Cloth, Laptop, Shoes
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'store/home.html', {})


def category_product(request, category):
    categories = {'Books': Book, 'MobilePhones': MobilePhone, 'Clothes': Cloth, 'Laptops': Laptop, 'Shoes': Shoes}
    model = categories[category]
    data = model.objects.all()
    return render(request, 'store/products/category-product.html', {'Category': category, 'data': data})


def product_detail(request, category, code):
    categories = {'Books': Book, 'MobilePhones': MobilePhone, 'Clothes': Cloth, 'Laptops': Laptop, 'Shoes': Shoes}
    model = categories[category]
    item = get_object_or_404(model, code=code)
    return render(request, 'store/products/product-detail.html', {"Category": category, "item": item})
