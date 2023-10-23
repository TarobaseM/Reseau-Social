from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect,get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect,HttpResponse
from .forms import PostForm
from django.shortcuts import redirect

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    form=CommentForm()
    
    return render(request, 'postapp/home.html', {'posts': posts,'like_post':like_post,'form':form})

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
def like_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return redirect('home')
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('home')  # Redirigez l'utilisateur vers la page d'accueil après avoir ajouté un commentaire

    return redirect('home')