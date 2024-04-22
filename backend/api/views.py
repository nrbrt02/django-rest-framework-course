from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.forms.models import model_to_dict
from products.models import Product
# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id','title'])

    # body = request.body
    # data = {}
    # try:
    #     data= json.loads(body)
    # except:
    #     pass
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # print(data)
    return Response(data)