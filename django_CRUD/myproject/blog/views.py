from django.shortcuts import redirect,render, get_object_or_404
from .models import Blog,Intro
from django.utils import timezone
from .forms import BlogUpdate
from django.core.paginator import Paginator
from faker import Faker
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
import accounts.views
# Create your views here.


def hello(request):
    return render(request,'hello.html')


#개발자 소개글
#1단계 간단한 글
#2단계 이미지 붙여보기

def intro(request):
    intro = Intro.objects
    return render(request,'intro.html',{'intro':intro})

def blog(request):
    blogs = Blog.objects
    
    #Blog를 쿼리셋으로 가져온다.
    blogs_list = Blog.objects.all()
    
    #가져온 걸 1개씩 잘라 페이지를 만든다.
    paginator = Paginator(blogs_list,5)

    #실제로 페이지에 들어갈 내용을 GET.get으로 가져옴
    page = request.GET.get('page')

    #그걸 이제 get_page로써 페이지를 뿌릴 것임.
    articles = paginator.get_page(page)

    return render(request,'blog.html',{'blogs':blogs, 'articles':articles})

def new(request):
    
    return render(request,'new.html')


def fake(request):
    for i in range(10):
        #faker로 만들어낸 글들을 블로그의
        #제목, 본문으로 넣자
        #1. Faker 객체 생성
        myfake = Faker()
        #2. 블로그 객체 생성
        fake = Blog()
        #3 fake의 메소드에 각각 대입
        fake.title = myfake.name()
        fake.body = myfake.sentence()
        fake.pub_date = timezone.datetime.now()
        fake.save()
    return redirect('/')

    
def create(request):
    blog = Blog()#Blog의 객체를 하나 생성
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    #image
    blog.images  = request.FILES.get('images',None)
    blog.writer = request.POST['writer']
    if blog.images is None:
        return render(request, 'new.html',{'error': 'please input images'})
    else:

        blog.pub_date = timezone.datetime.now()
    
        blog.save()
        #알림메세지 추가
        messages.success(request, 'Success to Upload')
        return redirect('/blog/'+str(blog.id))


def delete(request,blog_id):
    Blog.objects.get(id=blog_id).delete()
    return redirect('/')

def update(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    if request.method =='POST':
        form = BlogUpdate(request.POST)
            
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body= form.cleaned_data['body']
            blog.images = form.cleaned_data['images']
            blog.images = request.FILES['images']
            blog.pub_date = timezone.datetime.now()
            blog.save()#DB에 반영하기
            return redirect('/blog/'+str(blog.id))
            #redirect를 호출해서 객채를 호출해서 detail로 이동

    else:
        form = BlogUpdate(instance = blog)
        return render(request,'update.html',{'form':form})




def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html',{'blog' : blog_detail})