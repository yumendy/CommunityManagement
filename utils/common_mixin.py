from django.http import JsonResponse
from CommunityManagement.external_settings import COMMUNITY_NAME, COMMUNITY_DESCRIPTION, PAGE_NUMBER
from navbar.models import NavItem
from announcement.models import Announcement
from link.models import Link


class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        context['COMMUNITY_NAME'] = COMMUNITY_NAME
        context['COMMUNITY_DESCRIPTION'] = COMMUNITY_DESCRIPTION
        context['PAGE_NUMBER'] = PAGE_NUMBER
        return context


class FrontMixin(BaseMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(FrontMixin, self).get_context_data(**kwargs)
        context['nav_item_list'] = NavItem.objects.all()
        context['announcement_list'] = Announcement.objects.order_by('-create_time')[:3]
        context['link_list'] = Link.objects.all()
        return context


class AjaxableResponseMixin(BaseMixin):
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            data = {
                'state': 'error'
            }
            print form.errors
            return JsonResponse(data, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'state': 'success'
            }
            return JsonResponse(data)
        else:
            return response
