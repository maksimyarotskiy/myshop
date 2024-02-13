from django.db import models

from config import settings
from store.models import Product


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    discount_percent = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return f'product with discount: {self.product_name}, discount: {self.discount_percent}'

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='common_reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='common_reviews')
    product_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'Rating: {self.rating}, Product: {self.product_name}'
