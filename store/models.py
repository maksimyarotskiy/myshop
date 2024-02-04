from django.db import models
from django.contrib.auth.models import AbstractUser, User

from config import settings


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'

    def __str__(self):
        return f'photo: {self.image} for product:{self.product}'


class Order(models.Model):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.products


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'user:{self.user} about {self.product}'


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_user')
    products = models.ManyToManyField(Product, through='CartItem')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f'cart owner: {self.products} product:{self.products}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    def __str__(self):
        return f'product: {self.product}, cart: {self.cart}'


class UserProfile(AbstractUser):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    cart = models.OneToOneField(Cart, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_profile')

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return f'user address: {self.address}'


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_percent = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return f'product with discount: {self.product}, discount: {self.discount_percent}'
