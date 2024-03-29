from django.db import models
from django.conf import settings


class kicks(models.Model):
    # uuid that stock asigned for this product 
    # it's used to determine whether it's already in stock on the database

    uuid = models.CharField(max_length=100, )  # goat
    brand = models.CharField(max_length=100, null=True, blank=True, )
    category = models.CharField(max_length=100, null=True, blank=True, )  # goat
    product_type = models.CharField(max_length=300, null=True, blank=True, )  # goat
    colorway = models.CharField(max_length=150, null=True, blank=True, )  # goat
    countryOfManufacture = models.CharField(max_length=100, )
    dataType = models.CharField(max_length=100, )
    description = models.TextField()
    gender = models.CharField(max_length=10, default='')
    name = models.CharField(max_length=500, )  # goat
    name_kr = models.CharField(max_length=500, null=True)
    productCategory = models.CharField(max_length=100, )
    releaseDate = models.CharField(max_length=100, null=True, blank=True, default='2022-12-12')  # goat
    release_date_year = models.CharField(max_length=100, null=True, blank=True, )  # goat
    retailPrice = models.PositiveBigIntegerField(null=True, blank=True, )  # goat
    retailPriceKrw = models.PositiveBigIntegerField(null=True, blank=True, default=0)  # goat
    estimatedMarketValue = models.PositiveBigIntegerField(default=0)  # goat
    title = models.CharField(max_length=300, )
    sku = models.CharField(max_length=200, default=' ', null=True, blank=True, unique=True)  # ex) 555088-101# goat
    slug = models.CharField(max_length=500, default='', null=True, blank=True, )  # goat
    imageUrl = models.CharField(max_length=500, null=True, blank=True, )  # goat
    smallImageUrl = models.CharField(max_length=500, )
    thumbUrl = models.CharField(max_length=500, )

    local_imageUrl = models.CharField(max_length=500, default='media/images/defaultImg.png')
    local_smallImageUrl = models.CharField(max_length=500, default=' ')
    local_thumbUrl = models.CharField(max_length=500, default=' ')

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_users', blank=True)
    click = models.PositiveBigIntegerField(default=0)
    class Meta:
        indexes = [
            models.Index(fields=['id', 'brand']),
            models.Index(fields=['id', 'category']),
            models.Index(fields=['id', 'name']),
            models.Index(fields=['id', 'category', 'brand', 'name']),
            models.Index(fields=['id', 'brand', 'name']),
            models.Index(fields=['id', 'releaseDate']),
        ]

class productImg(models.Model):
    product = models.ForeignKey(kicks, on_delete=models.CASCADE, related_name='productImg')
    img_url = models.CharField(max_length=500, null=False, blank=False, )
    type = models.CharField(max_length=100, null=False,
                            blank=False, )  # left(main), right(main_sub), back, top, bottom, additional
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductCrawlingFlag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_item_cnt = models.PositiveIntegerField(default=0)
