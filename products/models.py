from django.db import models


class Category(models.Model):
    cat_id = models.CharField(max_length=15, primary_key=True)
    cat_name = models.CharField(max_length=20)
    pat_id = models.CharField(max_length=15, blank=True, null=True)  

    def __str__(self):
        return self.cat_name


class Brand(models.Model):
    b_id = models.CharField(max_length=5, primary_key=True)
    b_name = models.CharField(max_length=20)

    def __str__(self):
        return self.b_name


class Product(models.Model):
    p_id = models.CharField(max_length=5, primary_key=True)
    p_name = models.CharField(max_length=20)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='cat_id')
    b_id = models.ForeignKey(Brand, on_delete=models.CASCADE, to_field='b_id')
    image = models.URLField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    description = models.TextField(blank=True, null=True)  
    ratings = models.FloatField(default=0.0)  

    def __str__(self):
        return self.p_name
