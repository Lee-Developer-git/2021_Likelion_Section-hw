from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# 2. 사용할 모듈 불러오기
# 2-1 POST 형식의 HTTP 통신만 받기
from django.views.decorators.http import require_POST
# 2-2 response를 변환하는 가장 가본 함수, html 파일, 이미지 등 다양한 응답
from django.http import HttpResponse
# 2-3 딕셔너리를 json 형식으로 바꾸기 위해
import json


def main(request):
    items = Post.objects.all()
    return render(request, 'items/home.html', {'items': items})


def new(request):
    return render(request, 'items/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        Post.objects.create(title=title, content=content,
                            image=image, user=user)
    return redirect('main')


def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.view_count = post.view_count+1
    post.save()
    return render(request, 'items/show.html', {'post': post})


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('main')

# 3. like_toggle 함수 작성하기


@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # 포스트를 찾을 때 유용하게 사용되는 메서드
    post_like, post_like_created = Like.objects.get_or_create(
        user=request.user, post=post)

    # 좋아요를 누르지 않았다면, 눌렀다면
    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"

    context = {
        "like_count": post.like_count,
        "result": result
    }

    # 만든 context를 ajax에 json형태로 저장하겠다.
    return HttpResponse(json.dumps(context), content_type="application/json")
