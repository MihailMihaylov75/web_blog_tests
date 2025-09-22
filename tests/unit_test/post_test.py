__author__ = "Mihail Mihaylov"

import unittest
from post import Post


class TestPost(unittest.TestCase):
    def setUp(self) -> None:
        self.post = Post("Test", "Test Content")

    # --- init ---

    def test_post_title_is_set(self) -> None:
        """Asserts that the post title is set on init."""
        self.assertEqual("Test", self.post.title)

    def test_post_content_is_set(self) -> None:
        """Asserts that the post content is set on init."""
        self.assertEqual("Test Content", self.post.content)

    # --- json ---

    def test_json_has_correct_title(self) -> None:
        """Asserts that json() contains the correct title."""
        data = self.post.json()
        self.assertEqual("Test", data["title"])

    def test_json_has_correct_content(self) -> None:
        """Asserts that json() contains the correct content."""
        data = self.post.json()
        self.assertEqual("Test Content", data["content"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
