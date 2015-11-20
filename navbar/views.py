from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from utils.common_mixin import AjaxableResponseMixin, BaseMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from navbar.models import NavItem
from django.http import JsonResponse


class NavbarCreateView(AjaxableResponseMixin, CreateView):
    model = NavItem
    fields = ['title', 'show_order', 'url']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('navbar-list')

    def get_context_data(self, **kwargs):
        context = super(NavbarCreateView, self).get_context_data(**kwargs)
        context['active_page'] = 'navbar-add'
        return context


class NavbarListView(BaseMixin, ListView):
    model = NavItem
    context_object_name = 'navbar_list'

    def get_context_data(self, *args, **kwargs):
        context = super(NavbarListView, self).get_context_data(**kwargs)
        context['active_page'] = 'navbar-list'
        return context


class NavbarUpdateView(AjaxableResponseMixin, UpdateView):
    model = NavItem
    context_object_name = 'navitem'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('navbar-list')
    fields = ['title', 'show_order', 'url']

    def get_context_data(self, *args, **kwargs):
        context = super(NavbarUpdateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'navbar-update'
        return context


class NavbarDeleteView(AjaxableResponseMixin, DeleteView):
    model = NavItem
    success_url = reverse_lazy('navbar-list')

    def post(self, request, *args, **kwargs):
        super(NavbarDeleteView, self).post(self, request, *args, **kwargs)
        return JsonResponse({'state': 'success'})
