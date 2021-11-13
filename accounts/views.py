from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            Profile.objects.create(
                user=user,
                college=request.POST['college'],
                major=request.POST['major'],
            )
            auth.login(request, user)
            return redirect('/')
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
    return render(request, 'accounts/login.html')


def mypage(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        profile.college = request.POST['college']
        profile.major = request.POST['major']
        profile.save()
    return render(request, 'accounts/mypage.html')


def follow_manager(request, user_to_follow_id):
    follow_from = Profile.objects.get(user_id=request.user.id)
    follow_to = Profile.objects.get(user_id=user_to_follow_id)

    if follow_to in follow_from.following.all():
        follow_from.following.remove(follow_to)
    else:
        follow_from.following.add(follow_to)

    return redirect('/')
