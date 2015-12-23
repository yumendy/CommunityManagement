from django.core.urlresolvers import reverse_lazy
from utils.common_mixin import AjaxableResponseMixin, BaseMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from link.models import Link
from django.http import JsonResponse


# Create your views here.
class LinkCreateView(AjaxableResponseMixin, CreateView):
    model = Link
    fields = ['name', 'title', 'url', 'show_order']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('link-list')

    def get_context_data(self, *args, **kwargs):
        context = super(LinkCreateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'link-add'
        return context


class LinkListView(BaseMixin, ListView):
    model = Link
    context_object_name = 'link_list'

    def get_context_data(self, *args, **kwargs):
        context = super(LinkListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'link-list'
        return context


class LinkUpdateView(AjaxableResponseMixin, UpdateView):
    model = Link
    context_object_name = 'link'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('link-list')
    fields = ['name', 'title', 'url', 'show_order']

    def get_context_data(self, *args, **kwargs):
        context = super(LinkUpdateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'link-update'
        return context


class LinkDeleteView(AjaxableResponseMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')

    def post(self, request, *args, **kwargs):
        super(LinkDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})
