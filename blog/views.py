from django.shortcuts import render

def post_create(request):
    return render(request, 'blog/post_create.html')