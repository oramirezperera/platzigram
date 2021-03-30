""" Posts views """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Models
from posts.models import Posts

# Forms
from posts.forms import PostForm


# Create your views here.

class PostsFeedView(LoginRequiredMixin, ListView):
    """ Return all published posts """

    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('-created', )
    paginate_by = 30
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """ Specific Post Detail """

    template_name = 'posts/post_detail.html'
    queryset = Posts.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """ Create a new post """

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile

        return context
