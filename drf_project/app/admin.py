from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product, ProductShots

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( "id","name", "url")
    list_display_links = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( "id","title", "draft")
    list_display_links = ("title",)
    list_editable = ("draft",) 

@admin.register(ProductShots)
class ProductShotsAdmin(admin.ModelAdmin):
    list_display = ( "title", "image")
    list_display_links = ("title",)
    readonly_fields = ("get_image",)
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url } width="100" heigt="120"')