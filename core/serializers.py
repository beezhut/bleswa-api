from rest_framework import serializers, fields
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'mobile')

class WareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouse
        fields = ('id', 'name', 'address', 'latitide', 'longitude')

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('id', 'type', 'value', 'warehouse', 'status')

    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'mobile')

class LoanSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(queryset = Customer.objects.all(), source = 'customer',  write_only = True, allow_null = True)
    asset = AssetSerializer(read_only=True)
    asset_id = serializers.PrimaryKeyRelatedField(queryset = Asset.objects.all(), source = 'asset',  write_only = True, allow_null = True)

    class Meta:
        model = Loan
        fields = ('id', 'loan_account_number', 'type', 'sub_type', 'total_amount', 'balance_amount', 'customer', 'customer_id', 'asset', 'asset_id', 'branch')

class LoanMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('id', 'loan_account_number', 'type', 'sub_type', 'total_amount', 'balance_amount', 'customer', 'asset', 'branch')


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    loan = LoanMiniSerializer(read_only=True)
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
        fields = ('id', 'task_id', 'latitude', 'longitude', 'completed_time', 'status', 'feedback', 'collected_amount', 'payment_status')