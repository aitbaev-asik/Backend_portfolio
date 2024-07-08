from django.shortcuts import render, redirect
from .models import Experience, Education, Testimonial, Post, Project
from .forms import PostForm

def index(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    experiences = Experience.objects.all()
    education_list = Education.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        'experiences': experiences,
        'education_list': education_list,
        'testimonials': testimonials,
    }
    return render(request, 'mainapp/about.html', context)

def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'mainapp/blog.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'mainapp/projects.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'mainapp/create_post.html', {'form': form})
