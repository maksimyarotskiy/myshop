from django.contrib import admin
from store.models import *
from users.models import *
from common.models import *
from django.contrib.admin import TabularInline


class DiscountInline(TabularInline):
    model = Discount
    fields = ('discount_percent', 'start_date', 'end_date')
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1



@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'product', 'description', 'order')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description')
    #inlines = ('DiscountInline',)
    # inlines = [DiscountInline, ProductImageInline]
#    filter_horizontal = ('employees',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'rating', 'comment', 'date_posted')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'phone_number', 'cart')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'cart', 'quantity')

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'discount_percent', 'start_date', 'end_date')
