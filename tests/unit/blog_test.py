__author__ = 'Mihail Mihaylov'

import sys
import unittest

from blog import Blog


class TestBlog(unittest.TestCase):

    def setUp(self) -> None:
        self.blog = Blog('Test', 'Test Author')

    def tearDown(self) -> None:
        del self.blog

    def test_blog_creation(self):
        self.assertEqual('Test', self.blog.title)
        self.assertEqual('Test Author', self.blog.author)
        self.assertEqual([], self.blog.posts)

    def test_repr(self):
        blog2 = Blog('My day', 'Rolf')
        self.assertEqual(self.blog.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(blog2.__repr__(), 'My day by Rolf (0 posts)')

    def test_repr_multiple_posts(self):
        self.blog.posts.append('test post')
        self.assertEqual(self.blog.__repr__(), 'Test by Test Author (1 posts)')
        blog2 = Blog('My day', 'Rolf')
        blog2.posts.append('test1')
        blog2.posts.append('test2')
        self.assertEqual(blog2.__repr__(), 'My day by Rolf (2 posts)')


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=5, stream=sys.stdout))
