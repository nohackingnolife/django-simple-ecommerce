from django.urls import path
from .views import *


urlpatterns = [
    path('', StoreHome.as_view(), name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('<slug:product_slug>/', StoreProduct.as_view(), name='product'),
    path('category/<slug:category_slug>/', StoreCategory.as_view(), name='category'),
]
