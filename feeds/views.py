from django.shortcuts import redirect, render
from .models import Feed, Comment

# Create your views here.
def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.order_by('-id')
        return render(request, 'feeds/index.html', {'feeds': feeds})
    elif request.method == 'POST':
        # DB 에 저장하는 로직
        content = request.POST['content']
        Feed.objects.create(content=content)
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
    Comment.objects.create(feed_id=id, content=content)
    return redirect(f'/feeds/{id}')


def delete_comment(request, feed_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(f'/feeds/{feed_id}/')
