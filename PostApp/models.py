from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="images_postes/",blank=True,null=True)
    likes = models.ManyToManyField(User, related_name='liked_publications',null=True)
    shared_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"
    def total_likes(self):
        return self.likes.count()
    def get_image_width(self):
        with Post.open(self.image.path) as img:
            return img.width

    def get_image_height(self):
        with Post.open(self.image.path) as img:
            return img.height
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)