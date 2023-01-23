from django.contrib import admin

from network.models.contact import Contact
from network.models.factory import Factory
from network.models.private_trader import Private_trader
from network.models.products import Products
from network.models.retail_network import Retail_network


def delete_debts(modeladmin, request, queryset):
    queryset.update(debt=0)


delete_debts.short_description = "Удалить задолженности у выбранных объектов"


class FactoryAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'contacts',
                    'products',
                    'debt',
                    'created',
                    'updated'
                    )
    search_fields = ('title',
                     'contacts',
                     'products'
                     )
    list_filter = ('contacts__city',)
    actions = [delete_debts]


class Retail_networkAdmin(admin.ModelAdmin):

    list_display = ('title',
                    'contacts',
                    'products',
                    'debt',
                    'created',
                    'updated',
                    'view_supplier_link'
                    )
    search_fields = ('title',
                     'contacts',
                     'products',
                     'supplier'
                     )
    list_filter = ('contacts__city',)
    actions = [delete_debts]

    def view_supplier_link(self, obj):
        from django.utils.html import format_html
        url = 'http://127.0.0.1:8000/admin/network/factory/'+str(obj.id)+'/change/'
        return format_html('<a href="{}">Поставщик {}</a>', url, obj.id)

    view_supplier_link.short_description = "Поставщик"


class Private_traderAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'contacts',
                    'products',
                    'debt',
                    'created',
                    'updated',
                    'view_supplier_link'
                    )
    search_fields = ('title',
                     'contacts',
                     'products',
                     'supplier'
                     )
    list_filter = ('contacts__city',)
    actions = [delete_debts]

    def view_supplier_link(self, obj):
        from django.utils.html import format_html
        url = 'http://127.0.0.1:8000/admin/network/retail_network/'+str(obj.id)+'/change/'
        return format_html('<a href="{}">Поставщик {}</a>', url, obj.id)

    view_supplier_link.short_description = "Поставщик"


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email',
                    'country',
                    'city',
                    'street',
                    'house_number'
                    )
    search_fields = ('email',
                     'country',
                     'city',
                     'street',
                     'house_number'
                     )


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'model',
                    'created'
                    )
    search_fields = ('title',
                     'model',
                     'created'
                     )


admin.site.register(Factory, FactoryAdmin)
admin.site.register(Retail_network, Retail_networkAdmin)
admin.site.register(Private_trader, Private_traderAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Products, ProductsAdmin)
