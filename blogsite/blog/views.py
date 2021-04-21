from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse, Http404,JsonResponse
# Create your views here.
def HomeView(request):
    return render(request,'pages/home.html',context={}, status=200)

def List_blog_view(request,*args,**kwargs):
    qs= Blog.objects.all()
    blog_list=[{'id':i.id, 'content': i.content} for i in qs]
    data ={
        'response': blog_list
    }
    return JsonResponse(data)

def BlogView(request,blog_id,*args,**kwargs):
    data={
        'id': blog_id,
    }
    try:
        obj= Blog.objects.get(id=blog_id)
        data['content']= obj.content
        status=200
    except:
        data['message']='not found'
        status=404
    return JsonResponse(data,status=status)