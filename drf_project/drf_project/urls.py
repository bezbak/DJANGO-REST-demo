
from django.contrib import admin
from django.urls import path

from app.views import ProductAPIView,ProductShotsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/productlist/", ProductAPIView.as_view()),
    path("api/v1/productshotslist/", ProductShotsAPIView.as_view()),
]
