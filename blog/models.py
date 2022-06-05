from django.db import models
# from users.models import User


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title