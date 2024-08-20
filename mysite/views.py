from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import MainContent, Comment
from .forms import CommentForm
from .models import RecommProduct


#댓글 수정 및 삭제
@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)

    context = {'comment': comment, 'form': form}
    return render(request, 'mysite/comment_form.html', context)


@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('detail', content_id=comment.content_list.id)


#여기는 구독상품 페이지
def content_list(request):
    contents = MainContent.objects.all()
    return render(request, 'mysite/content_list.html', {'contents': contents})

def detail(request, content_id):
    content = get_object_or_404(MainContent, id=content_id)
    return render(request, 'mysite/content_detail.html', {'content': content})

#QnA 구역
@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content_list
            comment.author = request.user
            comment.save()
            return redirect('detail', content_id=content_list.id)
    else:
        form = CommentForm()


    context = {'content_list': content_list, 'form': form}
    return render(request, 'mysite/content_detail.html', context)



#추천상품 페이지
def recomm(request):
    contents = RecommProduct.objects.all()
    return render(request, 'mysite/recomm.html', {'contents': contents})

# 추천 상품 상세 페이지
def recomm_detail(request, content_id):
    content = get_object_or_404(RecommProduct, id=content_id)
    return render(request, 'mysite/recomm_detail.html', {'content': content})