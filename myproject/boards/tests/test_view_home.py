from django.test import TestCase
from django.urls import reverse, resolve
from ..models import Board
from ..views import BoardListView


class HomeTest(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('boards:home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        """Test the status code of the response."""
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """Test the url of home view. """
        view = resolve('/')
        self.assertEqual(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('boards:board_topics', kwargs={'id': self.board.id})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


