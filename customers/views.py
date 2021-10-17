from django.shortcuts import render

from customers.serializers import CustomerSerializer
from customers.models import Customer
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer 
    # permission_classes = [permissions.IsAuthenticated]