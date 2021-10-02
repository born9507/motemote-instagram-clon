from django.shortcuts import redirect, render
from .models import Feed

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
        return redirect('feeds:index')

def new(request):
    return render(request, 'feeds/new.html')
