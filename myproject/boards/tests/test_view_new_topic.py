from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views import new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm


class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description="Django boards.")
        User.objects.create_user(username='orlando1080', email='orlando1080@gmail.com', password='123')
        self.client.login(username='orlando1080', password='123')

    def test_new_topic_view_success_status_code(self):
        url = reverse('boards:new_topic', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_not_found_status_code(self):
        url = reverse('boards:new_topic', kwargs={'id': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new_topic/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('boards:new_topic', kwargs={'id': 1})
        board_topics_url = reverse('boards:board_topics', kwargs={'id': 1})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))

    def test_csrf(self):
        url = reverse('boards:new_topic', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('boards:new_topic', kwargs={'id': 1})
        data = {
            'subject': 'This is a story...',
            'message': 'All about how my life got flipped and turned upside down.',
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_contains_form(self):
        url = reverse('boards:new_topic', kwargs={'id': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewTopicForm)

    def test_new_topic_invalid_post_data(self):
        """Invalid post data should not redirect.
        The expected behavior is to show the form again with validation errors."""
        url = reverse('boards:new_topic', kwargs={'id': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_topic_invalid_post_data_empty_fields(self):
        """Invalid post data should not redirect.
        The expected behavior is to show the form again with validation errors."""
        url = reverse('boards:new_topic', kwargs={'id': 1})
        data = {
            'subject': '',
            'message': '',
        }
        response  = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())
