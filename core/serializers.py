from rest_framework import serializers, fields
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'mobile')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'mobile')

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('id', 'loan_account_number', 'type', 'amount')


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer()
    customer = CustomerSerializer()
    loan = LoanSerializer()

    class Meta:
        model = Task
        fields = ('id', 'assigned_to', 'customer', 'loan', 'status', 'description')