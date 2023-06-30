from django.contrib import admin
from .models import User, Customer, WareHouse, Asset, Branch, Loan, Task, Activity


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'mobile', 'designation', 'reporting_to']
    search_fields = ['first_name', 'last_name', 'email', 'mobile', 'reporting_to']
    list_filter = ['designation']

admin.site.register(User, UserAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile']
    search_fields = ['name', 'mobile']

admin.site.register(Customer, CustomerAdmin)



class WareHouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'longitude', 'latitude', 'address']
    search_fields = ['name']

admin.site.register(WareHouse, WareHouseAdmin)



class AssetAdmin(admin.ModelAdmin):
    list_display = ['type', 'value', 'warehouse', 'status']
    list_editable = ['status', 'warehouse']
    search_fields = ['type', 'warehouse', 'status']
    list_filter = ['type', 'status', 'warehouse']

admin.site.register(Asset, AssetAdmin)



class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'ifsc']
    search_fields = ['name', 'ifsc']

admin.site.register(Branch, BranchAdmin)



class LoanAdmin(admin.ModelAdmin):
    list_display = ['loan_account_number', 'type', 'total_amount', 'balance_amount', 'customer', 'branch']
    list_editable = ['branch']
    search_fields = ['loan_account_number', 'customer', 'branch', 'type']
    list_filter = ['type']

admin.site.register(Loan, LoanAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['loan', 'customer', 'assigned_to', 'status']
    list_editable = ['status']
    search_fields = ['loan', 'customer', 'assigned_to', 'staus']
    list_filter = ['status']

admin.site.register(Task, TaskAdmin)


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['task', 'status', 'payment_status', 'completed_time', 'longitude', 'latitude']
    list_editable = ['status', 'payment_status']
    search_fields = ['task', 'status']
    list_filter = ['status', 'payment_status']

admin.site.register(Activity, ActivityAdmin)