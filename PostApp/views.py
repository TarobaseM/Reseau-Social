from django.contrib.auth.decorators import login_required


# Create your views here.
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect
from .forms import PostForm
@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'postapp/home.html', {'posts': posts})

@login_required
def poster(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user  # Assuming you're using authentication
            new_post.save()
            return redirect('home')  # Redirect to your homepage or a suitable URL

    else:
        form = PostForm()

    return render(request, 'postapp/poster.html', {'form': form})
