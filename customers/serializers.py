from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['nike_name']
