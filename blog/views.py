from django.shortcuts import redirect, render
from blog.forms import PostForm
from django.contrib.auth import logout, login
from django.contrib import messages

def post_create(request):
    post_form = PostForm()
    
    if request.method == "POST" :
        post_form = PostForm(request.POST)
        
        if post_form.is_valid():
            post_form.save()
            return redirect("home")
            
    context = {
        "post_form": post_form,
    }

    return render(request, 'blog/post_create.html', context)