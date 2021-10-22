from django.shortcuts import render
from .models import Product,ProductCategory,ProductImages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View, DetailView, ListView
from django.db.models import Prefetch
# Create your views here.
from django.core.paginator import Paginator

class CategoryView(DetailView):

    model = ProductCategory
    #template_name='products/productcatgeory_list.html'

    def get_queryset(self):
        queryset = super(CategoryView, self).get_queryset()
        queryset = ProductCategory.objects.prefetch_related(
            Prefetch(
                'product_set',
                queryset=Product.objects.all().prefetch_related(
                    Prefetch(
                        'productimages_set',
                        queryset=ProductImages.objects.filter(is_default=True)
                    )        
                )
            )        
        ).filter(
            slug__icontains=self.kwargs['slug']
        )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productcategory'] = context['productcategory']
        context['category_products'] = context['productcategory'].product_set.all()
        return context
    

class ProductListView(ListView):

    model = Product
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category = ProductCategory.objects.get(slug__icontains=self.kwargs['slug'])
        queryset = Product.objects.filter(category=category).prefetch_related(
                            Prefetch(
                                'productimages_set',
                                queryset=ProductImages.objects.filter(is_default=True)
                            )        
                        )   
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['productcategory'] = ProductCategory.objects.get(slug__icontains=self.kwargs['slug'])
        context['category_products'] = context['products']
        return context
    

class ProductDetail(DetailView):

    model = Product

    def get_queryset(self):
        queryset = super(ProductDetail, self).get_queryset()
        queryset = Product.objects.prefetch_related(
            Prefetch(
                'productimages_set',
                queryset=ProductImages.objects.all().order_by('is_default')
            )        
        ).filter(
            slug__icontains=self.kwargs['slug']
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_obj = context['product']
        related_product = Product.objects.prefetch_related(
            Prefetch(
                'productimages_set',
                queryset=ProductImages.objects.filter(is_default=True)
            )        
        ).filter(
            category_id=product_obj.category_id,            
        ).exclude(
            id__in=[product_obj.pk]
        )

        context['related_product'] = related_product
        return context
    