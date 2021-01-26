
from django.http import JsonResponse, response
from .models import Product, Manufacturer

def product_list(request):
    products = Product.objects.all() 
    data = {"products": list(products.values())}  # "pk","name"
    response =JsonResponse(data)
    return response

def product_detail(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product" : {
            "name" : product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.productdescription,
            "product code": product.productcode,
            "price": product.price,
            "photo": product.photo.url,
            "quantity": product.quantity,

        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
            response = JsonResponse({
                "error" : {
                    "code" : 404,
                    "message" : "Product is Not Found !"
            }},
            status = 404)
    return response


#from django.views.generic.detail import DetailView
#from django.views.generic.list import ListView

#from .models import Product,Manufacturer
# Create your views here.

#class ProductDetailView(DetailView):
#   model = Product
# template_name = "products/product_detail.html"

#class ProductListView(ListView):
#model = Product
#template_name = "products/product_list.html"

    
