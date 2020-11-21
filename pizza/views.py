
from rest_framework import generics
from .models import Pizza
from.serializer import PizzaSerializer


class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    def get_queryset(self):
        shape = self.request.query_params.get('shape', None)
        size = self.request.query_params.get('size', None)
        queryset = Pizza.objects.all()
        if shape is not None:
            queryset = queryset.filter(shape=shape)
        if size is not None:
            queryset = queryset.filter(size=size)
        return queryset


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

