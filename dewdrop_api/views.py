from rest_framework import generics
from dewdrop.models import Condition, Product, ProductConditionSolution
from .serializers import ProductSerializer, ConditionSerializer, ProductConditionSolutionSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pass

class ConditionList(generics.ListCreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    pass

class ProductConditionSolutionList(generics.ListCreateAPIView):
    queryset = ProductConditionSolution.objects.all()
    serializer_class = ProductConditionSolution
    pass