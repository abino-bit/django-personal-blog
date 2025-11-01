from django.shortcuts import render
import random

# Lists of blogs and images
BLOGS = [
    "Today I learned about Django views and templates. It's amazing how Django separates logic from presentation!",
    "Just finished building my first web application. The feeling of seeing your code come to life is incredible.",
    "Explored the world of web development today. CSS makes everything look so much better!",
    "Working on understanding URL routing in Django. It's like creating a map for your website.",
    "Another day, another line of code. Progress may be slow, but every step counts in this journey.",
]

IMAGES = [
    "https://picsum.photos/400/300?random=1",
    "https://picsum.photos/400/300?random=2",
    "https://picsum.photos/400/300?random=3",
    "https://picsum.photos/400/300?random=4",
    "https://picsum.photos/400/300?random=5",
]


def blog(request):
    """Display a random blog post and image"""
    context = {
        'blog': random.choice(BLOGS),
        'image': random.choice(IMAGES),
    }
    return render(request, 'blog/blog.html', context)


def show_all(request):
    """Display all blog posts and images"""
    context = {
        'blogs': BLOGS,
        'images': IMAGES,
    }
    return render(request, 'blog/show_all.html', context)


def about(request):
    """Display about page"""
    context = {
        'name': 'Abino Deogracious',
        'bio': 'I am a beginner web developer learning Django and Python.',
        'interests': ['Web Development', 'Python', 'Django', 'Learning New Things'],
    }
    return render(request, 'blog/about.html', context)