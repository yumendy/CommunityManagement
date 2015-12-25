from django.http import JsonResponse
from CommunityManagement.external_settings import COMMUNITY_NAME, COMMUNITY_DESCRIPTION, PAGE_NUMBER
from navbar.models import NavItem
from announcement.models import Announcement
from link.models import Link
from activity.models import Activity


class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        context['COMMUNITY_NAME'] = COMMUNITY_NAME
        context['COMMUNITY_DESCRIPTION'] = COMMUNITY_DESCRIPTION
        context['PAGE_NUMBER'] = PAGE_NUMBER
        return context


class NavMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(NavMixin, self).get_context_data(**kwargs)
        context['nav_item_list'] = NavItem.objects.all()
        return context


class AnnouncementMixin(object):
    def get_context_data(self, **kwargs):
        context = super(AnnouncementMixin, self).get_context_data(**kwargs)
        context['announcement_list'] = Announcement.objects.order_by('-create_time')[:3]
        return context


class LinkMixin(object):
    def get_context_data(self, **kwargs):
        context = super(LinkMixin, self).get_context_data(**kwargs)
        context['link_list'] = Link.objects.all()
        return context


class UserMixin(object):
    def get_context_data(self, **kwargs):
        context = super(UserMixin, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['myuser'] = self.request.user.myuser
        return context


class ActivityMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ActivityMixin, self).get_context_data(**kwargs)
        context['activity_list'] = Activity.objects.order_by('-start_time')
        return context


class FrontMixin(BaseMixin, NavMixin, AnnouncementMixin, LinkMixin, UserMixin):
    def get_context_data(self, *args, **kwargs):
        context = super(FrontMixin, self).get_context_data(**kwargs)
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
