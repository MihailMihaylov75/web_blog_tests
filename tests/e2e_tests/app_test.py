__author__ = "Mihail Mihaylov"

import unittest
from unittest.mock import patch

import app
from blog import Blog
from post import Post


class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        blog = Blog("Test", "Test author")
        app.blogs = {"Test": blog}

    def tearDown(self) -> None:
        app.blogs.clear()

    # --- menu dispatch ---

    def test_menu_calls_ask_create_blog(self) -> None:
        with patch("builtins.input") as mocked_input, patch("app.ask_create_blog") as mocked:
            mocked_input.side_effect = ("c", "Test Create Blog", "Test Author", "q")
            app.menu()
            mocked.assert_called()

    def test_menu_calls_print_blogs(self) -> None:
        with patch("builtins.input") as mocked_input, patch("app.print_blogs") as mocked:
            mocked_input.side_effect = ("l", "q")
            app.menu()
            mocked.assert_called()

    def test_menu_calls_ask_read_blog(self) -> None:
        with patch("builtins.input") as mocked_input, patch("app.ask_read_blog") as mocked:
            mocked_input.side_effect = ("r", "Test", "q")
            app.menu()
            mocked.assert_called()

    def test_menu_calls_ask_create_post(self) -> None:
        with patch("builtins.input") as mocked_input, patch("app.ask_create_post") as mocked:
            mocked_input.side_effect = ("p", "Test", "X", "Y", "q")
            app.menu()
            mocked.assert_called()

    # --- menu initial prints ---

    def test_menu_prints_existing_blogs_on_start(self) -> None:
        with patch("builtins.print") as mocked_print, patch("builtins.input", return_value="q"):
            app.menu()
            mocked_print.assert_called_with("- Test by Test author (0 posts)")

    def test_menu_prints_prompt(self) -> None:
        with patch("builtins.input", return_value="q") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    # --- print_blogs / print_post(s) ---

    def test_print_blogs_prints_single_blog(self) -> None:
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Test by Test author (0 posts)")

    def test_print_post_formats_output(self) -> None:
        expected = app.POST_TEMPLATE.format("Post title", "Post content")
        with patch("builtins.print") as mocked_print:
            app.print_post("Post title", "Post content")
            mocked_print.assert_called_with(expected)

    # --- create/read blog ---

    def test_ask_create_blog_creates_entry(self) -> None:
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("New Blog", "Author A")
            app.ask_create_blog()
            self.assertIn("New Blog", app.blogs)

    def test_ask_read_blog_calls_print_posts(self) -> None:
        with patch("builtins.input", return_value="Test"), patch("app.print_posts") as mocked_print:
            app.ask_read_blog()
            mocked_print.assert_called_with(app.blogs["Test"])

    # --- create post (split into two tests, one assert each) ---

    def test_ask_create_post_appends_post_title(self) -> None:
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test author", "Test Content")
            app.ask_create_post()
            self.assertEqual(app.blogs["Test"].posts[0].title, "Test author")

    def test_ask_create_post_appends_post_content(self) -> None:
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test author", "Test Content")
            app.ask_create_post()
            self.assertEqual(app.blogs["Test"].posts[0].content, "Test Content")

    def test_ask_read_blog_handles_missing(self) -> None:
        with patch("builtins.input", return_value="Missing"), patch("builtins.print") as mocked_print:
            app.ask_read_blog()
            mocked_print.assert_called_with('No blog found with title "Missing".')

    def test_ask_create_post_handles_missing(self) -> None:
        with patch("builtins.input", return_value="Missing"), patch("builtins.print") as mocked_print:
            app.ask_create_post()
            mocked_print.assert_called_with('No blog found with title "Missing".')


if __name__ == "__main__":
    unittest.main(verbosity=2)
