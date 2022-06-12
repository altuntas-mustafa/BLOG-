from django.db import models
from django.utils.text import slugify
from users.models import User
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.category_name

class Status(models.Model):
    status = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.status

class Post(models.Model):   
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length=800, blank=False)
    category = models.ForeignKey(Category,max_length=30,on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null= False, blank=True, unique=True, db_index=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True
    )
    def like_count(self):
        return self.like_set.all().count()
        
    def __str__(self):
        return f"{self.title}"

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()
    

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def str(self):
        return self.user.username
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username