from django.core.urlresolvers import reverse_lazy
from utils.common_mixin import AjaxableResponseMixin, BaseMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from carousel.models import Carousel
from django.http import JsonResponse


class CarouselCreateView(AjaxableResponseMixin, CreateView):
    model = Carousel
    fields = ['title', 'summery', 'img', 'target_url', 'show_order', 'on_show']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('carousel-list')

    def get_context_data(self, *args, **kwargs):
        context = super(CarouselCreateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'carousel-add'
        return context


class CarouselListView(BaseMixin, ListView):
    model = Carousel
    context_object_name = 'carousel_list'

    def get_context_data(self, *args, **kwargs):
        context = super(CarouselListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'carousel-list'
        return context


class CarouselUpdateView(AjaxableResponseMixin, UpdateView):
    model = Carousel
    context_object_name = 'carousel'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('carousel-list')
    fields = ['title', 'summery', 'img', 'target_url', 'show_order', 'on_show']

    def get_context_data(self, *args, **kwargs):
        context = super(CarouselUpdateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'carousel-update'
        return context


class CarouselDeleteView(AjaxableResponseMixin, DeleteView):
    model = Carousel
    success_url = reverse_lazy('carousel-list')

    def post(self, request, *args, **kwargs):
        super(CarouselDeleteView, self).post(self, request, *args, **kwargs)
        return JsonResponse({'state': 'success'})
