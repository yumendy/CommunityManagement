from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from carousel.models import Carousel
from utils.common_mixin import BaseMixin, FrontMixin
from article.models import Blog


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
        context['carousel_list'] = Carousel.objects.filter(on_show=True)
        context['article_list'] = Blog.objects.order_by('-modification_time')[:5]
        if Blog.objects.all().count() > 5:
            context['has_more_article'] = True
        return context

    def get(self, request, *args, **kwargs):
        if not request.COOKIES.get('has_viewed_index_page', False):
            return HttpResponseRedirect(reverse('index_page'))
        else:
            return super(HomepageView, self).get(request, *args, **kwargs)


class DashboardOverviewView(BackMixin, TemplateView):
    template_name = 'website/backend/dashboard/overview.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardOverviewView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'overview'
        return context


class SettingsOverviewView(BackMixin, TemplateView):
    template_name = 'website/backend/settings/overview.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SettingsOverviewView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'overview'
        return context
