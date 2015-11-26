from django.shortcuts import render
from article.models import Category, Essay
from utils.common_mixin import AjaxableResponseMixin, BaseMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class CategoryCreateView(AjaxableResponseMixin, CreateView):
    pass


class CategoryListView(BaseMixin, ListView):
    pass


class CategoryUpdateView(AjaxableResponseMixin, UpdateView):
    pass


class CategoryDeleteView(AjaxableResponseMixin, DeleteView):
    pass


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
