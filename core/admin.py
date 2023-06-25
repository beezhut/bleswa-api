from django.contrib import admin
from .models import User, Customer, WareHouse, Asset, Branch, Loan

admin.site.register(User)

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
    list_display = ['loan_account_number', 'type', 'amount', 'customer', 'branch']
    list_editable = ['branch']
    search_fields = ['loan_account_number', 'customer', 'branch', 'type']
    list_filter = ['type']

admin.site.register(Loan, LoanAdmin)


admin.site.site_header = 'Bleswa Solutions'