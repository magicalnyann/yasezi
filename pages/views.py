from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Lounge, Comments, Reply
from django.db.models import Prefetch
from .forms import LoungeForm, CommentForm, ReplyForm
from django.http import JsonResponse




def commu(request):
    lounges = Lounge.objects.all().order_by('-pub_date')
    paginator = Paginator(lounges, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'pages/commu.html', {'page_obj': page_obj})

#게시판 글 추가
def add_lounge(request):
    if request.method == 'POST':
        form = LoungeForm(request.POST, request.FILES)
        if form.is_valid():
            lounge = form.save(commit=False)
            if lounge.is_anonymous:
                lounge.author = None
            else:
                lounge.author = request.user
            lounge.save()  # Save the lounge instance to the database
            return redirect('commu')
    else:
        form = LoungeForm()
    return render(request, 'pages/add_lounge.html', {'form': form})


#게시판 상세 보기
def commu_detail(request, lounge_id):
    lounge = get_object_or_404(Lounge, id=lounge_id)
    
    comments = Comments.objects.filter(content_list=lounge).prefetch_related(
        Prefetch('reply_replies', queryset=Reply.objects.all())
    )
    
    context = {
        'lounge': lounge,
        'comments': comments,
        'form': CommentForm()
    }
    
    return render(request, 'pages/commu_detail.html', context)

#게시판 수정
def lounge_edit(request, lounge_id):
    lounge = get_object_or_404(Lounge, id=lounge_id)

    if request.method == 'POST':
        form = LoungeForm(request.POST, request.FILES, instance=lounge)
        if form.is_valid():
            form.save()
            return redirect('commu')
    else:
        form = LoungeForm(instance=lounge)

    return render(request, 'pages/lounge_edit.html', {'form': form})




def lounge_del(request, lounge_id):
    lounge = get_object_or_404(Lounge, id=lounge_id)

    if request.method == 'POST':
        lounge.delete()

        return redirect('commu')

    return redirect('commu')




#게시글 좋아요 싫어요
def like_lounge(request, lounge_id):
    lounge = get_object_or_404(Lounge, id=lounge_id)
    lounge.likes += 1
    lounge.save()
    return JsonResponse({'likes': lounge.likes})


def dislike_lounge(request, lounge_id):
    lounge = get_object_or_404(Lounge, id=lounge_id)
    lounge.dislikes += 1
    lounge.save()
    return JsonResponse({'dislikes': lounge.dislikes})


# 댓글 작성
def make_comments(request, lounge_id):
    lounge = get_object_or_404(Lounge, id=lounge_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = lounge 
            comment.author = request.user
            comment.save()
            return redirect('commu_detail', lounge_id=lounge.id)
    else:
        form = CommentForm()

    return render(request, 'pages/commu_detail.html', {'form': form, 'lounge': lounge})


# 대댓글 작성
def dedet(request, lounge_id, parent_comment_id):
    lounge = get_object_or_404(Lounge, id=lounge_id)
    parent_comment = get_object_or_404(Comments, id=parent_comment_id)

    if request.method == 'POST':
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.content_list = lounge
            reply.author = request.user
            reply.parent_comment = parent_comment  
            reply.save()
            return redirect('commu_detail', lounge_id=lounge.id)
    else:
        form = ReplyForm()
    
    return render(request, 'pages/commu_detail.html', {'form': form, 'lounge': lounge, 'parent_comment': parent_comment})


#댓글 좋아요
def toggle_like(request, comment_id):
    comment = get_object_or_404(Comments, id=comment_id)
    if request.user.is_authenticated:
        if request.user in comment.liked_by.all():
            comment.liked_by.remove(request.user)
            comment.heart -= 1
        else:
            comment.liked_by.add(request.user)
            comment.heart += 1
        comment.save()
    return redirect(request.META.get('HTTP_REFERER', 'commu_detail'))



#대댓글 좋아요 
def toggle_reply_like(request, reply_id):
    reply = get_object_or_404(Comments, id=reply_id)
    if request.user.is_authenticated:
        if request.user in reply.liked_by.all():
            reply.liked_by.remove(request.user)
            reply.heart -= 1
        else:
            reply.liked_by.add(request.user)
            reply.heart += 1
        reply.save()
    return redirect(request.META.get('HTTP_REFERER', 'commu_detail'))         