
from django.db import models

# Create your models here.


class Category(models.Model):
    "Категории"
    name = models.CharField("Категория",max_length=150)
    description =models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    title = models.CharField("Название продукта",max_length=255)
    description = models.TextField(blank=True)
    draft = models.BooleanField("Черновик", default=False)
    cat = models.ForeignKey(Category, verbose_name="Category",on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField('Цена', default=0)
    oc = models.CharField("Операционная система",max_length=255,null=True)
    pros = models.CharField("Процессор",max_length=255,null=True)
    ram = models.CharField("Оперативка",max_length=255,null=True)
    vidyha = models.CharField("Видеокарта",max_length=255,null=True)
    storage = models.CharField("Место на диске",max_length=255,null=True)
    region = models.CharField("Регион",max_length=255,null=True)
    activate= models.CharField("Сервис активации",max_length=255, null=True)

    def __str__(self):
        return self.title

    
class ProductShots(models.Model):
    "Product shots"
    title = models.CharField("The title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="movie_shots/")
    Product = models.ForeignKey(Product.__name__, verbose_name="Movie", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Product shot"
        verbose_name_plural = "Product shots"
