import unittest

from blog import Blog


class TestBlog(unittest.TestCase):
    def setUp(self) -> None:
        self.blog = Blog('Test', 'Test Author')

    def tearDown(self) -> None:
        del self.blog

    def test_create_post_in_blog(self):
        self.blog.create_post('Test post', 'Test Content')
        self.assertEqual(len(self.blog.posts), 1)
        self.assertEqual(self.blog.posts[0].title, 'Test post')
        self.assertEqual(self.blog.posts[0].content, 'Test Content')

    def test_json_no_post(self):
        expected = {'title': 'Test',
                    'author': 'Test Author',
                    'posts': []}
        self.assertDictEqual(expected, self.blog.json())

    def test_json(self):
        self.blog.create_post('Test post', 'Test Content')
        expected = {'title': 'Test',
                    'author': 'Test Author',
                    'posts': [{'title': 'Test post',
                               'content': 'Test Content'}]}
        self.assertDictEqual(expected, self.blog.json())


if __name__ == '__main__':
    unittest.main()
