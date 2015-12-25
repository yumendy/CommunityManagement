# coding=utf-8
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from authentication.models import Department, MyUser
from utils.common_mixin import AjaxableResponseMixin, BaseMixin, FrontMixin
from forms import LoginForm


class DepartmentCreateView(AjaxableResponseMixin, CreateView):
    model = Department
    fields = ['name']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('department-list')

    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentCreateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'department-add'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(DepartmentCreateView, self).form_valid(form)


class DepartmentListView(BaseMixin, ListView):
    model = Department
    context_object_name = 'department_list'

    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'department-list'
        return context


class DepartmentUpdateView(AjaxableResponseMixin, UpdateView):
    model = Department
    context_object_name = 'department'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('department-list')
    fields = ['name']

    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentUpdateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'department-update'
        return context


class DepartmentDeleteView(AjaxableResponseMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('department-list')

    def post(self, request, *args, **kwargs):
        super(DepartmentDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})


class LogoutView(RedirectView):
    pattern_name = 'homepage'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class LoginView(FrontMixin, FormView):
    template_name = 'authentication/user_login.html'
    success_url = reverse_lazy('homepage')
    form_class = LoginForm

    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'login'
        return context

    def form_valid(self, form):
        user = form.login()
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return super(LoginView, self).form_valid(form)
            else:
                return self.response_error_page('你的账户尚未激活')
        else:
            return self.response_error_page('用户名或密码错误')

    def response_error_page(self, msg):
        return render(self.request, 'utils/error_page.html', {'message': msg})


class ApplyView(FrontMixin, CreateView):
    model = MyUser
    fields = ['name', 'student_id', 'college', 'tel', 'is_public_tel', 'sex', 'level', 'birthday', 'qq', 'is_public_qq',
              'description', 'photo']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('user-login')

    def get_context_data(self, *args, **kwargs):
        context = super(ApplyView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'sign-up'
        return context

    def form_valid(self, form):
        username = form.data.get('username', '')
        password = form.data.get('password', '')
        email = form.data.get('email', '')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False
        user.save()
        form.instance.user = user
        return super(ApplyView, self).form_valid(form)

    def form_invalid(self, form):
        print form.errors
        return super(ApplyView, self).form_invalid(form)


class UnauthorizedUserListView(BaseMixin, ListView):
    queryset = MyUser.objects.filter(user__is_active=False).order_by('id')
    template_name = 'authentication/unauthorized_user_list.html'
    paginate_by = 20
    context_object_name = 'user_list'

    def get_context_data(self, *args, **kwargs):
        context = super(UnauthorizedUserListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'myuser-unauthorized-list'
        return context


class UserUpdateView(UpdateView):
    model = MyUser
    fields = ['name', 'student_id', 'college', 'tel', 'is_public_tel', 'sex', 'level', 'birthday', 'qq', 'is_public_qq',
              'description', 'photo']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('homepage')
    context_object_name = 'myuser'

    def get_context_data(self, *args, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['active_page'] = 'myuser-update'
        return context

    def form_valid(self, form):
        email = form.data.get('email', '')
        user = self.object.user
        user.email = email
        user.save()
        return super(UserUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        print form.errors
        return super(UserUpdateView, self).form_invalid(form)


class UserListView(BaseMixin, ListView):
    queryset = MyUser.objects.filter(user__is_active=True).order_by('level')
    template_name = 'authentication/user_list.html'
    paginate_by = 20
    context_object_name = 'user_list'

    def get_context_data(self, *args, **kwargs):
        context = super(UserListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'myuser-list'
        return context


class UserDetailView(BaseMixin, DetailView):
    model = MyUser
    template_name = 'authentication/myuser_detail.html'
    context_object_name = 'user'

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'myuser-detail'
        return context


class UserDeleteView(AjaxableResponseMixin, DeleteView):
    pass


class AuthorizeUserView(AjaxableResponseMixin, FormView):
    def post(self, request, *args, **kwargs):
        user = MyUser.objects.get(pk=kwargs['pk'])
        user.user.is_active = True
        user.user.save()
        return JsonResponse({'state': 'success'})
