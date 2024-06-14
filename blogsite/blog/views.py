from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Santiago Ocampo',
        'title': 'Blog Post 1',
        'content': 'This is my first blog post',
        'date_posted': '12th June, 2024',
    },

    {
        'author': 'Santiago Ocampo',
        'title': 'Blog Post 2',
        'content': 'This is my second blog post',
        'date_posted': '13th June, 2024',
    }
]

def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})

def login(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})