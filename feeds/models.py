from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User

class Feed(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_feeds', through='Like')

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.content

    def seed(count):
        myfake = Faker('ko_KR')
        for i in range(count):
            Feed.objects.create(content=myfake.catch_phrase())


class Comment(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, related_name='comment_set', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', related_name='child_comment_set', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'[feed: {self.feed}] {self.content}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
