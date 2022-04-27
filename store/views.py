from django.core import paginator
from django.http.response import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import *


class StoreHome(ListView):
    paginate_by = 12
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_cheker'] = 0
        search_query = self.request.GET.get('search', '')
        context['search_query'] = search_query
        if search_query:
            context['products'] = Product.objects.filter(title__icontains=search_query)
            context['category_cheker'] = -1
            if len(context['products']) == 0:
                context['category_cheker'] = -2

        context['categories'] = Category.objects.all()
        context['index_title'] = 'Народная Аптека – Ваша аптека иностранных лекарств и медикаментов. Купить в Украине, Киеве, Харькове, Одессе'
        context['index_description'] = 'Народная Аптека онлайн – лучший сервис для покупки лекарств и медикаментов из иностранных стран. Бесплатная доставка во все города Украины: Киев, Харьков, Одесса и другие. Самые низкие цены рынке, доставим быстро, легко и удобно!'

        return context

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class StoreCategory(ListView):
    paginate_by = 12
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category_cheker'] = context['products'][0].category_id
        context['index_title'] = f'Народная Аптека – Ваша аптека иностранных лекарств и медикаментов. Купить {context["products"][0].category} в Украине, Киеве, Харькове, Одессе'
        context['index_description'] = f'Народная Аптека онлайн – лучший сервис для покупки лекарств и медикаментов из иностранных стран. Бесплатная доставка во все города Украины: Киев, Харьков, Одесса и другие. Самые низкие цены рынке, доставим быстро, легко и удобно! Купить {context["products"][0].category} в Украине'
        return context

    def get_queryset(self):
        return Product.objects.filter(is_published=True, category__slug=self.kwargs['category_slug'])
    

def about(request):
    return render(request, 'store/about.html')

def contacts(request):
    return render(request, 'store/contacts.html', context={'phone': Phone.objects.all()[0]})


class StoreProduct(DetailView):
    model = Product
    template_name = 'store/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
