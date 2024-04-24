from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializers
# Create your views here.

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)