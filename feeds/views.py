from django.shortcuts import redirect, render
from .models import Feed, Comment, Like

# Create your views here.
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.order_by('-id')
        return render(request, 'feeds/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        # DB 에 저장하는 로직
        content = request.POST['content']
        Feed.objects.create(content=content, author=request.user)
        # feed = Feed(content=content)
        # feed.save()
        return redirect('/')

def new(request):
    return render(request, 'feeds/new.html')

def show(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feeds/show.html', {'feed': feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/')

def update(request, id):
    if request.method == 'GET':
        feed = Feed.objects.get(id=id)
        return render(request, 'feeds/update.html', {'feed': feed})
    if request.method == "POST":
        Feed.objects.filter(id=id).update(content=request.POST['content'])

        return redirect(f'/feeds/{id}/')


def create_comment(request, id):
    content = request.POST['content']
    Comment.objects.create(feed_id=id, content=content, author=request.user)
    return redirect(f'/feeds/{id}')


def delete_comment(request, feed_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(f'/feeds/{feed_id}/')


def create_nested_comment(request, feed_id, comment_id):
    feed = Feed.objects.get(id=feed_id)
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        Comment.objects.create(
            feed_id=feed_id,
            parent_comment_id=comment_id,
            content=request.POST['content']
        )
        return redirect(f"/feeds/{feed_id}/")
    return render(request, 'feeds/new_nested_comment.html', {'feed': feed, 'comment': comment})


def like(request, id):
    feed = Feed.objects.get(id=id)
    is_liked_by_me = feed.like_users.filter(id=request.user.id).exists()
    if is_liked_by_me:
        feed.like_users.remove(request.user)
    else:
        feed.like_users.add(request.user)
        # Like.objects.create(user=request.user, feed=feed)
    return redirect ('/')
