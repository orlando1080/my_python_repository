from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from ..models import Board, Post, Topic
from ..views import reply_topic
from ..forms import PostForm


class ReplyTopicTestCase(TestCase):
    """Base test case to be used in all 'reply_topic' view tests."""
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django Board.')
        self.username = 'orlando1080'
        self.password = 'finsihingtouch7'
        user = User.objects.create_user(username=self.username, email='orlando1080@gmail.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello world', board=self.board, start=user)
        Post.objects.create(message='Testing123', topic=self.topic, created_by=user)
        self.url = reverse('boards:reply_topic', kwargs={'id': self.board.id, 'topic_id': self.topic.id})


class LoginRequiredReplyTopicTests(ReplyTopicTestCase):
    def test_redirection(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, f'{login_url}?next={self.url}')


class ReplyTopicTests(ReplyTopicTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/boards/1/topics/1/reply/')
        self.assertEquals(view.func, reply_topic)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contain_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, PostForm)

    def test_form_inputs(self):
        """The view must contain two inputs: csrf, message textarea."""
        self.assertContains(self.response, '<input', 1)
        self.assertContains(self.response, '<textarea', 1)


class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {'message': 'hello, world!'})

    def test_redirection(self):
        """A valid form submission should redirect the user."""
        url = reverse('boards:topic_posts', kwargs={'id': self.board.id, 'topic_id': self.topic.id})
        topic_posts_url = f'{url}?page=1#2'
        self.assertRedirects(self.response, topic_posts_url)

    def test_reply_created(self):
        """The total post count should be 2. The one created in the 'ReplyTopicTestCase' setUp and another created
        by the post data in this class."""
        self.assertEquals(Post.objects.count(), 2)


class InvalidReplyTopicTests(ReplyTopicTestCase):
    def setUp(self):
        """Submit an empty dictionary to the 'reply_topic' view."""
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {})

    def test_status_code(self):
        """An invalid form submission should return to the same page."""
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

