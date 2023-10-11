from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="images_postes/",blank=True,null=True)
    
    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"
