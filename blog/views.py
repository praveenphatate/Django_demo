from django.shortcuts import render


# Create your views here.
posts = [
    {
        'author': 'Praveen Phatate',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Jan 4, 2023',
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'First Post Content',
        'date_posted': 'Jan 28, 2023',
    },
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
