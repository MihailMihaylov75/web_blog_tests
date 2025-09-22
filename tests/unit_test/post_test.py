__author__ = 'Mihail Mihaylov'
import unittest

from post import Post


class PostTest(unittest.TestCase):
    def test_create_post(self):
        post = Post('Test', 'Test Content')
        self.assertEqual('Test', post.title)
        self.assertEqual('Test Content', post.content)

    def test_json(self):
        post = Post('Test', 'Test Content')
        expected = {'title': 'Test',
                    'content': 'Test Content'}

        self.assertDictEqual(expected, post.json())
