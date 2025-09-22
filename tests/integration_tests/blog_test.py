__author__ = "Mihail Mihaylov"

import unittest
from blog import Blog


class TestBlogIntegration(unittest.TestCase):
    def setUp(self) -> None:
        self.blog = Blog("Test", "Test Author")

    def tearDown(self) -> None:
        del self.blog

    # --- create_post (split) ---

    def test_create_post_increments_count(self) -> None:
        """After creating a post, the number of posts is 1."""
        self.blog.create_post("Test post", "Test Content")
        self.assertEqual(1, len(self.blog.posts))

    def test_create_post_sets_title(self) -> None:
        """Created post has the correct title."""
        self.blog.create_post("Test post", "Test Content")
        self.assertEqual("Test post", self.blog.posts[0].title)

    def test_create_post_sets_content(self) -> None:
        """Created post has the correct content."""
        self.blog.create_post("Test post", "Test Content")
        self.assertEqual("Test Content", self.blog.posts[0].content)

    # --- json with no posts (split) ---

    def test_json_no_post_has_title(self) -> None:
        """JSON has correct blog title when there are no posts."""
        self.assertEqual("Test", self.blog.json()["title"])

    def test_json_no_post_has_author(self) -> None:
        """JSON has correct blog author when there are no posts."""
        self.assertEqual("Test Author", self.blog.json()["author"])

    def test_json_no_post_has_empty_posts(self) -> None:
        """JSON has empty posts list when there are no posts."""
        self.assertEqual([], self.blog.json()["posts"])

    # --- json with one post (split) ---

    def test_json_one_post_includes_single_post(self) -> None:
        """JSON includes exactly one post after creation."""
        self.blog.create_post("Test post", "Test Content")
        self.assertEqual(1, len(self.blog.json()["posts"]))

    def test_json_one_post_has_correct_title(self) -> None:
        """JSON has correct title for the single post."""
        self.blog.create_post("Test post", "Test Content")
        self.assertEqual("Test post", self.blog.json()["posts"][0]["title"])

    def test_json_one_post_has_correct_content(self) -> None:
        """JSON has correct content for the single post."""
        self.blog.create_post("Test post", "Test Content")
        self.assertEqual("Test Content", self.blog.json()["posts"][0]["content"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
