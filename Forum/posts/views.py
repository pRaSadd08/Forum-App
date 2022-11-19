from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForms
# Create your views here.



def index(request):
    #if method is post
    if request.method =='POST':
        form = PostForms(request.POST)
      # if the from is valid
        if form.is_valid(): 
        #yes,Save
          form.save()
        # redirect to home
          return HttpResponseRedirect('/')
        
        #no, Show Error
        else:
          return HttpResponseRedirect(form.errors_as_jason())
    
    
    
    #Get all posts limit = 20
    posts = Post.objects.all()[:20]
    return render(request, 'posts.html',
                  {'posts':posts})