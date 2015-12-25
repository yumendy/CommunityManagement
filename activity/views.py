from django.core.urlresolvers import reverse_lazy
from activity.models import Activity, Task, Actor
from utils.common_mixin import AjaxableResponseMixin, BaseMixin, FrontMixin
from django.db.models import Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from CommunityManagement.external_settings import PAGE_NUMBER


class ActivityCreateView(AjaxableResponseMixin, CreateView):
    model = Activity
    template_name_suffix = '_create_form'
    fields = ['title', 'content', 'responsible_user', 'address']
    success_url = reverse_lazy('activity-list')

    def get_context_data(self, *args, **kwargs):
        context = super(ActivityCreateView, self).get_context_data(*args, **kwargs)
        context['user_list'] = User.objects.filter(is_active=True)
        context['active_page'] = 'activity-add'
        return context

    def form_valid(self, form):
        form.instance.start_time = form.data['start_time'].replace('T', ' ')
        form.instance.closing_time = form.data['closing_time'].replace('T', ' ')
        form.instance.entry_closing_time = form.data['entry_closing_time'].replace('T', ' ')
        return super(ActivityCreateView, self).form_valid(form)


class ActivityListView(BaseMixin, ListView):
    model = Activity
    context_object_name = 'activity_list'
    queryset = Activity.objects.order_by('-start_time').annotate(actor_number=Count('actor'))

    def get_context_data(self, *args, **kwargs):
        context = super(ActivityListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'activity-list'
        return context


class ActivityUpdateView(AjaxableResponseMixin, UpdateView):
    model = Activity
    template_name_suffix = '_update_form'
    fields = ['title', 'content', 'responsible_user', 'address']
    success_url = reverse_lazy('activity-list')
    context_object_name = 'activity'

    def get_context_data(self, *args, **kwargs):
        context = super(ActivityUpdateView, self).get_context_data(*args, **kwargs)
        context['user_list'] = User.objects.filter(is_active=True)
        context['active_page'] = 'activity-update'
        return context

    def form_valid(self, form):
        form.instance.start_time = form.data['start_time'].replace('T', ' ')
        form.instance.closing_time = form.data['closing_time'].replace('T', ' ')
        form.instance.entry_closing_time = form.data['entry_closing_time'].replace('T', ' ')
        return super(ActivityUpdateView, self).form_valid(form)


class ActivityDeleteView(AjaxableResponseMixin, DeleteView):
    model = Activity
    success_url = reverse_lazy('activity-list')

    def post(self, request, *args, **kwargs):
        super(ActivityDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})


class ActivityDetailView(FrontMixin, DetailView):
    model = Activity
    context_object_name = 'activity'
    template_name = 'activity/activity_detail.html'


class TaskCreateView(AjaxableResponseMixin, CreateView):
    pass


class TaskListView(BaseMixin, ListView):
    pass


class TaskUpdateView(AjaxableResponseMixin, UpdateView):
    pass


class TaskDeleteView(AjaxableResponseMixin, DeleteView):
    pass


class TaskDetailView(BaseMixin, DetailView):
    pass


class ActorCreateView(AjaxableResponseMixin, FrontMixin, CreateView):
    model = Actor
    template_name_suffix = '_create_form'
    fields = ['name', 'student_id', 'sex', 'level', 'tel']

    def get_context_data(self, *args, **kwargs):
        context = super(ActorCreateView, self).get_context_data(*args, **kwargs)
        context['activity'] = Activity.objects.get(pk=self.kwargs.get('activity_id'))
        return context

    def form_valid(self, form):
        form.instance.activity = Activity.objects.get(pk=self.kwargs.get('activity_id'))
        return super(ActorCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('activity-detail', kwargs={'pk': self.kwargs.get('activity_id')})


class ActorListView(BaseMixin, ListView):
    template_name = 'activity/actor_list.html'
    context_object_name = 'actor_list'
    model = Actor

    def get_context_data(self, *args, **kwargs):
        context = super(ActorListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'actor-list'
        context['activity'] = Activity.objects.get(pk=self.kwargs.get('activity_id'))
        return context

    def get_queryset(self):
        queryset = Actor.objects.filter(activity=Activity.objects.get(pk=self.kwargs.get('activity_id')))
        return queryset


class ActorDeleteView(AjaxableResponseMixin, DeleteView):
    model = Actor
    success_url = reverse_lazy('activity-list')

    def post(self, request, *args, **kwargs):
        super(ActorDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})

