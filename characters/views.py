from django.shortcuts import render
from django.http import HttpRequest, Http404
from django.core.paginator import Paginator
from characters.data import posts
from django.contrib.auth.decorators import login_required
    
# Create your views here.
@login_required(login_url='/auth/login/')
def characters(request):
    postPaginator = Paginator(posts, 20)
    page_num = request.GET.get('page')
    page = postPaginator.get_page(page_num)
    
    return render(request=request, 
                  template_name='characters/index.html',
                  context={
                      'text': 'Almanaque Rick and Morty',
                      'title': 'Characters',
                      'page': page,
                  })

@login_required(login_url='/auth/login/')
def character(request: HttpRequest, post_id:int):
    found_post = None
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404("Post não existe")
    
    return render(request=request, 
                  template_name='characters/post.html',
                  context={
                      'post': found_post,
                      'title': post["name"],
                  })
    