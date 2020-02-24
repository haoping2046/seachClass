import requests
from django.shortcuts import render

from .models import Product

from .forms import ProductForm, RawProductForm


# Create your views here.

# 调用自定义的RawProductForm方法（没有字段验证，只有Django里的判断是否为空条件）
# def product_create_view(request):
#
# 	my_form = RawProductForm()
# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 			my_form = ProductForm()
# 		else:
# 			print(my_form.errors)
#
# 	context = {
# 		"form": my_form
# 	}
# 	return render(request, "products/products_create.html", context)

# 给字段加验证, 调用自定义的ProductForm方法
def product_create_view(request):
	url = "https://api.gugudata.com/weather/weatherinfo?appkey=YOUR_APPKEY&code=YOUR_VALUE&days=1"
	payload = {}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	print(response.text.encode('utf8'))

    # form = ProductForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = ProductForm()
	#
    # context = {
    #     'form': form
    # }
    # return render(request, "products/products_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    # 	'title': obj.title,
    # 	'description': obj.description,
    # 	'price': obj.price,
    # 	'summary': obj.summary,
    # 	'featured': obj.featured,
    # }
    context = {
        'object': obj
    }
    return render(request, "products/products_detail.html", context)


def render_initial_data(request):
	initial_data = {
		'title': "My this awesome title"
	}

	obj = Product.objects.get(id=2)

	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "products/products_create.html", context)


