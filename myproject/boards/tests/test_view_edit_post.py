from django.forms import ModelForm

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

from ..models import Board, Post, Topic
from ..views import PostUpdateView


class PostUpdateViewTestCase(TestCase):
    """Base test case to be used in all 'PostUpdateView' view tests"""
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django boards.')
        self.username = 'orlando1080'
        self.password = 'finishingtouch7'
        user = User.objects.create_user(username=self.username, email='orlando1080@gmail.com', password=self.password)
        self.topic = Topic.objects.create(subject='Hello, world', board=self.board, start=user)
        self.post = Post.objects.create(message='This is a story all about', topic=self.topic, created_by=user)
        self.url = reverse('boards:edit_post', kwargs={
                            'id': self.board.id,
                            'topic_id': self.topic.id,
                            'post_pk': self.post.pk,
        })


class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
    """Test if only logged-in users can edit the post."""
    def test_redirection(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, f'{login_url}?next={self.url}')


class UnauthorizedPostUpdateViewTests(PostUpdateViewTestCase):
    """Create a new user different from the one who posted."""
    def setUp(self):
        super().setUp()
        username = 'sonic'
        password = 'abc123'
        user = User.objects.create_user(username=username, email='sonic@gmail.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        """A topic should be edited only by the owner. Unauthorized users should get 404 response (Page Not Found)."""
        self.assertEquals(self.response.status_code, 404)


class PostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve('/boards/1/topics/1/posts/1/edit/')
        self.assertEquals(view.func.view_class, PostUpdateView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ModelForm)

    def test_form_inputs(self):
        """The view must contain two iputs: csrf, message textarea"""
        self.assertContains(self.response, '<input', 1)
        self.assertContains(self.response, '<textarea', 1)


class SuccessfulPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {'message': 'edited message'})

    def test_redirection(self):
        """A valid form submission should redirect the user."""
        topic_posts_url = reverse('boards:topic_posts', kwargs={'id': self.board.id, 'topic_id': self.topic.id})
        self.assertRedirects(self.response, topic_posts_url)

    def test_post_change(self):
        self.post.refresh_from_db()
        self.assertEquals(self.post.message, 'edited message')


class InvalidPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        """Submit an empty dictionary to the 'reply_topic' view."""
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {})

    def test_status_code(self):
        """An invalid form submission should return to the same page."""
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form =self.response.context.get('form')
        self.assertTrue(form.errors)

