from . import views
from django.urls import path

app_name = 'boards'

urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    path('boards/<int:id>/', views.TopicListView.as_view(), name='board_topics'),
    path('boards/<int:id>/new_topic/', views.new_topic, name='new_topic'),
    path('boards/<int:id>/topics/<int:topic_id>/', views.PostListView.as_view(), name='topic_posts'),
    path('boards/<int:id>/topics/<int:topic_id>/reply/', views.reply_topic, name='reply_topic'),
    path('boards/<int:id>/topics/<int:topic_id>/posts/<int:post_pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
]
