from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from navbar.models import NavItem
from utils.common_mixin import BaseMixin


class FrontMixin(BaseMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(FrontMixin, self).get_context_data(**kwargs)
        context['nav_item_list'] = NavItem.objects.all()
        return context


class BackMixin(BaseMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(BackMixin, self).get_context_data(**kwargs)
        return context


class IndexView(FrontMixin, TemplateView):
    template_name = 'website/index.html'


class HomepageView(FrontMixin, TemplateView):
    template_name = 'website/homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'home-page'
        return context

    def get(self, request, *args, **kwargs):
        if not request.COOKIES.get('has_viewed_index_page', False):
            return HttpResponseRedirect(reverse('index_page'))
        else:
            return super(HomepageView, self).get(request, *args, **kwargs)


class DashboardOverviewView(BackMixin, TemplateView):
    template_name = 'website/dashboard/overview.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardOverviewView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'overview'
        return context
