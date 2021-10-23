from django.db import models
from django.utils import timezone
from faker import Faker

# Create your models here.
class Feed(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

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
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'[feed: {self.feed}] {self.content}'
