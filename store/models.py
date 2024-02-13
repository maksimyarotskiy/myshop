from django.db import models

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
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'

    def __str__(self):
        return f'photo: {self.image} for product:{self.product}'

class Order(models.Model):
    products = models.ManyToManyField('store.Product')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.pk)

class Review(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'user:{self.user} about {self.product}'

class Cart(models.Model):
    user = models.OneToOneField('users.UserProfile', on_delete=models.CASCADE, related_name='cart_user')
    products = models.ManyToManyField('store.Product', through='CartItem')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f'cart owner: {self.user}'

class CartItem(models.Model):
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('store.Cart', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

    def __str__(self):
        return f'product: {self.product}, cart: {self.cart}'
