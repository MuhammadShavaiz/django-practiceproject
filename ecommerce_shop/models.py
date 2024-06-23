from django.db import models
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50 , default="")
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='ecommerce_shop/images', default="")

    def __str__(self):
        return self.product_name
