from django.core.checks.messages import Error
from blog.forms import PostForm, CommentForm, HashtagForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Hashtag, Post
from django.utils import timezone

# Create your views here.

#메인페이지
def main(request):
    return render(request, 'main.html')

#글쓰기페이지
def write(request):
    return render(request, 'write.html')

#글쓰기 함수
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            form.save_m2m()
            return redirect('read')
    else:
        form = PostForm
        return render(request, 'write.html', {'form':form})

#읽기페이지
def read(request):
    posts = Post.objects
    hashtags = Hashtag.objects
    return render(request, 'read.html', {'posts':posts, 'hashtags':hashtags})

#디테일페이지 댓글함수
def detail(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('detail', id)
    else:
        form=CommentForm()
        return render(request, 'detail.html', {'post':post, 'form':form} )

#수정페이지
def edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})


#삭제 함수
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('read')

#해시태그 함수
def hashtagform(request, hashtag=None):
    if request.method == "POST":
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'hashtag.html', {'form':form, "error_message":error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('main')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'hashtag.html', {'form':form} )

#검색 함수
def search(request, hashtag_id):
    blog = Post.objects
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    return render(request, 'search.html', {'blog':blog, 'hashtag':hashtag})