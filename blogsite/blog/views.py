from django.shortcuts import render, redirect
from .models import Blog
from .forms import Create_form
from django.http import HttpResponse, Http404,JsonResponse, HttpResponseRedirect
# Create your views here.
def blog_create_view(request, *args,**kwargs):
    next_url= request.POST.get('next') or None
    form = Create_form(request.POST or None)
    if form.is_valid():
        obj= form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form= Create_form()
    return render(request,'components/form.html',context={'form':form})



def HomeView(request):
    return render(request,'pages/home.html',context={}, status=200)

def List_blog_view(request,*args,**kwargs):
    qs= Blog.objects.all()
    blog_list=[{'id':i.id, 'content': i.content, 'content_title': i.content_title} for i in qs]
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