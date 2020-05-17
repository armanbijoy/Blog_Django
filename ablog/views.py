from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import *
from .form import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
def LikeView(request, pk):
    post = get_object_or_404(Blog, id= request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))
    
    
class Bloglist(ListView):
    model = Blog
    template_name = 'home.html'
    ordering = ['-id']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Bloglist, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Blog, id=self.kwargs[pk])
        total_likes = stuff.total_likes()
        context['cat_menu']= cat_menu
        context['total_likes'] = total_likes
        
        return context

def CategoryView(request,cats):
    cat_post = Blog.objects.filter(category=cats)
    return render(request,'category_views.html', {'cats': cats, 'cat_post': cat_post})


class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogUpdate(UpdateView):
    model = Blog
    template_name = 'update.html'
    form_class = BlogForm
    # fields = '__all__'
class BlogCreate(CreateView):
    model = Blog
    template_name = 'addpost.html'
    form_class = AddForm
    # fields = '__all__'
class CategoryCreate(CreateView):
    model = Category
    template_name = 'category.html'
    fields = '__all__'

class BlogDelete(DeleteView):
    model = Blog
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')
    

