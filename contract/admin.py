from django.contrib import admin
from contract.models import *
from contract.views import *


# Register your models here.
@admin.register(company)
class companyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'bank', 'address']
    list_display_links = ['title']


@admin.register(contact_information)
class contact_informationAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'address', 'phone']
    list_display_links = ['person']


@admin.register(client)
class clientAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'address', 'person']
    list_display_links = ['title']


@admin.register(unit)
class unitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['name']


@admin.register(type)
class typeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['name']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'advantage', 'advantage']
    list_display_links = ['name']


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'nickname', 'unit', 'cost_price', 'min_selling_price', 'meno']
    list_display_links = ['name']


@admin.register(product_info)
class product_infoAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', ]
    list_display_links = ['product']


@admin.register(payment_info)
class payment_infoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['name']


@admin.register(contract_info)
class contract_infoAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return contract_info_views(request)


admin.site.site_header = '斯康企业管理平台0.1'
admin.site.site_title = '斯康企业管理平台0.1'
