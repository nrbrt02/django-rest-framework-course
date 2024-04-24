from rest_framework import generics

from .models import Product
from .serializers import ProductSerializers

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    # def perform_create(self, serializer):
    #     # return super().perform_create(serializer)
    #     print(serializer)
    #     serializer.save()

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)
        