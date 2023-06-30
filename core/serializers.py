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
        fields = ('id', 'loan_account_number', 'type', 'total_amount', 'balance_amount')


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    loan = LoanSerializer(read_only=True)
    assignee_id = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), source = 'assigned_to',  write_only = True, allow_null = True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset = Customer.objects.all(), source = 'customer',  write_only = True, allow_null = True)
    loan_id = serializers.PrimaryKeyRelatedField(queryset = Loan.objects.all(), source = 'loan', write_only = True, allow_null = True)

    class Meta:
        model = Task
        fields = ('id', 'assigned_to', 'assignee_id', 'customer', 'customer_id', 'loan', 'loan_id', 'status', 'description')        


class ActivitySerializer(serializers.ModelSerializer):
    task_id = serializers.PrimaryKeyRelatedField(queryset = Task.objects.all(), source = 'task', allow_null = True)

    class Meta:
        model = Activity
        fields = ('task_id', 'latitude', 'longitude', 'completed_time', 'status', 'feedback', 'collected_amount', 'payment_status')