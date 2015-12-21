from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from article.models import Category, Blog, PurePage
from utils.common_mixin import AjaxableResponseMixin, BaseMixin, FrontMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse, Http404
from CommunityManagement.external_settings import PAGE_NUMBER


class CategoryCreateView(AjaxableResponseMixin, CreateView):
    model = Category
    fields = ['name']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('category-list')

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'category-add'
        return context


class CategoryListView(BaseMixin, ListView):
    model = Category
    context_object_name = 'category_list'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'category-list'
        return context


class CategoryUpdateView(AjaxableResponseMixin, UpdateView):
    model = Category
    context_object_name = 'category'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('category-list')
    fields = ['name']

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'category-update'
        return context


class CategoryDeleteView(AjaxableResponseMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')

    def post(self, request, *args, **kwargs):
        super(CategoryDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})


class BlogCreateView(AjaxableResponseMixin, CreateView):
    model = Blog
    template_name_suffix = '_create_form'
    fields = ['title', 'content', 'category']
    success_url = reverse_lazy('blog-list-personal')

    def get_context_data(self, *args, **kwargs):
        context = super(BlogCreateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'blog-add'
        context['category_list'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.show_times = 0
        return super(BlogCreateView, self).form_valid(form)


class PersonalBlogListView(BaseMixin, ListView):
    context_object_name = 'essay_list'
    template_name = 'article/blog_list.html'

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(PersonalBlogListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'blog-list'
        return context


class BlogUpdateView(AjaxableResponseMixin, UpdateView):
    model = Blog
    context_object_name = 'blog'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('blog-list-personal')
    fields = ['title', 'category', 'content']

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        blog = Blog.objects.get(pk=kwargs.get('pk'))
        if blog.author != user:
            raise Http404
        else:
            return super(BlogUpdateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(BlogUpdateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'blog-update'
        context['category_list'] = Category.objects.all()
        return context


class BlogDeleteView(AjaxableResponseMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog-list-personal')

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        blog = Blog.objects.get(pk=kwargs.get('pk'))
        if blog.author != user:
            raise Http404
        else:
            return super(BlogDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        super(BlogDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})


class BlogDetailView(FrontMixin, DetailView):
    model = Blog
    context_object_name = 'article'
    template_name = 'article/article_detail.html'


class BlogListView(FrontMixin, ListView):
    model = Blog
    context_object_name = 'article_list'
    template_name = 'article/article_list.html'
    paginate_by = PAGE_NUMBER


class PurePageCreateView(AjaxableResponseMixin, CreateView):
    model = PurePage
    template_name_suffix = '_create_form'
    fields = ['title', 'content']
    success_url = reverse_lazy('pure-page-list')

    def get_context_data(self, *args, **kwargs):
        context = super(PurePageCreateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'pure-page-add'
        return context


class PurePageUpdateView(AjaxableResponseMixin, UpdateView):
    model = PurePage
    template_name_suffix = '_update_form'
    context_object_name = 'page'
    fields = ['title', 'content']
    success_url = reverse_lazy('pure-page-list')

    def get_context_data(self, *args, **kwargs):
        context = super(PurePageUpdateView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'pure-page-update'
        return context


class PurePageDeleteView(AjaxableResponseMixin, DeleteView):
    model = PurePage
    success_url = reverse_lazy('pure-page-list')

    def post(self, request, *args, **kwargs):
        super(PurePageDeleteView, self).post(request, *args, **kwargs)
        return JsonResponse({'state': 'success'})


class PurePageListView(BaseMixin, ListView):
    model = PurePage
    context_object_name = 'page_list'
    template_name = 'article/purepage_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PurePageListView, self).get_context_data(*args, **kwargs)
        context['active_page'] = 'pure-page-list'
        return context


class PurePageDetailView(FrontMixin, DetailView):
    model = PurePage
    context_object_name = 'article'
    template_name = 'article/article_detail.html'
