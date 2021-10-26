from django.urls import path
from . import views

app_name = 'feeds'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:feed_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:id>/like/', views.like, name='like'),
    # localhost:8000/feeds/10/like/
]
