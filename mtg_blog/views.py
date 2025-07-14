from django.shortcuts import render
from django.db.models import Count
from .models import Topic

def home(request):
    topics = (
        Topic.objects
        .annotate(
            num_posts = Count('posts'))
        .order_by('-num_posts')[:10]
    )
    return render(request, 'mtg_blog_app/home.html', {'topics': topics})
