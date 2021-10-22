from django.urls import path,include
from .models import Product, ProductCategory
from .views import ProductDetail,CategoryView,ProductListView


urlpatterns=[
    path('<slug:slug>/',ProductDetail.as_view(),name='product_detail'),
    path('category/<slug:slug>/', ProductListView.as_view(), name='category_view')
]