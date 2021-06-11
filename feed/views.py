from django.views.generic import TemplateView, DetailView, FormView
#ccbv.co.uk for help with Templateview and detailview etc..
from .models import Post
from .forms import PostForm
from django.contrib import messages




# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

def dispatch(self, request, *args, **kwargs):
    self.request = request
    return super().dispatch(request, *args, **kwargs)


class AddPostView(FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        new_object = Post.objects.create(
            title = form.cleaned_data['title'],
            image=form.cleaned_data['image'],
            text=form.cleaned_data['description'],
            
        )
        messages.add_message(self.request, messages.SUCCESS, 'Post Submitted!' )
        return super().form_valid(form)
        

class AboutPageView(TemplateView):  # new
    template_name = 'about.html'

  

        


    


