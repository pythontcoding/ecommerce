from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.views.generic.base import TemplateResponseMixin,TemplateResponse
from django.core.mail import send_mail
from products.models import Product, ProductCategory,ProductImages,SliderManager
from django.db.models import Prefetch

from .form import ContactForm

def index(request):
    
    product_query_set = Product.objects.prefetch_related(
        Prefetch(
            'productimages_set',
            queryset=ProductImages.objects.filter(is_default=True)
        )
    ).filter(
        is_offer=True
    )
    slider_manager = SliderManager.objects.filter(status=True)
    context = {
        'page_title': 'HomePage',
        'product_lists':product_query_set,
        'slider_manager':slider_manager
    }

    return render(request,'home-page.html',context)


class ContactUs(TemplateView):

    template_name = 'contact-us.html'
    form_class = ContactForm

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        context['form'] = self.form_class
        return self.render_to_response(context)

    def post(self, request, *args,**kwargs):

        context = self.get_context_data(**kwargs)

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email_address = form.cleaned_data['email_address']
            message = form.cleaned_data['message']

            send_mail('subject','message','priyankachauhansingh27@gmail.com', [email_address])

            return redirect('thank_you')

        else:
            print('Form is not valid')

        context['form'] = form
        return self.render_to_response(context)

        
def thank_you(request):

    return HttpResponse('Email has been send successfully!')
