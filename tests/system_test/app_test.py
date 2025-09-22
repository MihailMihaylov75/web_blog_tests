import unittest
from unittest.mock import patch

import app
from blog import Blog
from post import Post


class TestApp(unittest.TestCase):

    def setUp(self):
        blog = Blog('Test', 'Test author')
        app.blogs = {'Test': blog}

    def test_menu_call_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
                app.menu()
                mocked_create_blog.assert_called()

    def test_menu_call_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:
                mocked_input.side_effect = ('l', 'Test Create Blog', 'Test Author', 'q')
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_call_ask_read_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_read_blog:
                mocked_input.side_effect = ('r', 'Test Create Blog', 'Test Author', 'q')
                app.menu()
                mocked_read_blog.assert_called()

    def test_menu_call_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_input.side_effect = ('p', 'Test Create Blog', 'Test Author', 'q')
                app.menu()
                mocked_ask_create_post.assert_called()

    def test_menu_prints_blogs(self):
        with patch('builtins.print') as mocked_print:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print.assert_called_with('- Test by Test author (0 posts)')

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()

            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print:
                app.ask_read_blog()
                mocked_print.assert_called_with(app.blogs['Test'])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = app.POST_TEMPLATE.format('Post title', 'Post content')

        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        blog = app.blogs['Test']
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test author', 'Test Content')
            app.ask_create_post()
            self.assertEqual(blog.posts[0].title, 'Test author')
            self.assertEqual(blog.posts[0].content, 'Test Content')


if __name__ == '__main__':
    unittest.main()
