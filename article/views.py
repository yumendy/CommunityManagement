from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from article.models import Category, Essay
from utils.common_mixin import AjaxableResponseMixin, BaseMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse


class CategoryCreateView(AjaxableResponseMixin, CreateView):
    model = Category
    fields = ['name']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('category-list')

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'category-add'
        return context


class CategoryListView(BaseMixin, ListView):
    model = Category
    context_object_name = 'category_list'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'category-list'
        return context


class CategoryUpdateView(AjaxableResponseMixin, UpdateView):
    model = Category
    context_object_name = 'category'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('category-list')
    fields = ['name']

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'category-update'
        return context


class CategoryDeleteView(AjaxableResponseMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')

    def post(self, request, *args, **kwargs):
        super(CategoryDeleteView, self).post(*args, **kwargs)
        return JsonResponse({'state': 'success'})


class ArticleCreateView(AjaxableResponseMixin, CreateView):
    pass


class ArticleListView(BaseMixin, ListView):
    pass


class ArticleUpdateView(AjaxableResponseMixin, UpdateView):
    pass


class ArticleDeleteView(AjaxableResponseMixin, DeleteView):
    pass


class ArticleDetailView(BaseMixin, DetailView):
    pass
