from django.contrib import admin
from .models import Post, Category,Status,Comment,PostView,Like

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)