

# Create your views here.
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'postapp/home.html', {'posts': posts})
def poster(request):
    print("test")
    return render(request)