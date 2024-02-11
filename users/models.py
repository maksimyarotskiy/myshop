# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# from store.models import Product
#
# class UserProfile(AbstractUser):
#     address = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=20)
#
#     class Meta:
#         verbose_name = 'UserProfile'
#         verbose_name_plural = 'UserProfiles'
#
#     def __str__(self):
#         return f'user address: {self.address}'
#
#
# class Cart(models.Model):
#     user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart_user')
#     products = models.ManyToManyField(Product, through='CartItem')
#
#     class Meta:
#         verbose_name = 'Cart'
#         verbose_name_plural = 'Carts'
#
#     def __str__(self):
#         return f'cart owner: {self.products} product:{self.products}'
#
#
# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     class Meta:
#         verbose_name = 'CartItem'
#         verbose_name_plural = 'CartItems'
#
#     def __str__(self):
#         return f'product: {self.product}, cart: {self.cart}'
#
