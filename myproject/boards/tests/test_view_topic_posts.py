from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board, Post, Topic
from ..views import PostListView


class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Django', description='Django board.')
        user = User.objects.create_user(username='orlando1080', email='orlando1080@gmail.com',
                                        password='finishingtouch7')
        topic = Topic.objects.create(subject='Carpe diem!', board=board, start=user)
        Post.objects.create(message='Seize the moment!', topic=topic, created_by=user)
        url = reverse('boards:topic_posts', kwargs={'id': board.id, 'topic_id': topic.id})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/boards/1/topics/1/')
        self.assertEquals(view.func.view_class, PostListView)
