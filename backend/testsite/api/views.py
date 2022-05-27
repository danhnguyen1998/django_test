from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed"}, status=405)
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)