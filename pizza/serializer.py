from rest_framework import serializers
from .models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','toppings','shape','size')
        model = Pizza
