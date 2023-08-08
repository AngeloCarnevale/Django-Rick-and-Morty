from django.shortcuts import render
from django.http import HttpRequest, Http404
from blog.data import posts


# Create your views here.
def blog(request):
    return render(request=request, 
                  template_name='blog/index.html',
                  context={
                      'text': 'Almanaque Rick and Morty',
                      'title': 'Characters',
                      'posts': posts,
                  })
    
def post(request: HttpRequest, post_id: int):
    
    found_post = None
        
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404("Post não existe")
    
    return render(request=request, 
                  template_name='blog/post.html',
                  context={
                      'post': found_post,
                  })
    