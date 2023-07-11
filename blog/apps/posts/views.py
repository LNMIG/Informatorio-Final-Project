from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request,'posts/home.html')

def post(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post.html', context)