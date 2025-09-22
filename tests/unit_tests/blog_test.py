__author__ = "Mihail Mihaylov"

import unittest
from blog import Blog


class TestBlog(unittest.TestCase):
    def setUp(self) -> None:
        self.blog = Blog("Test", "Test Author")

    # --- creation ---

    def test_blog_title_is_set(self) -> None:
        """Asserts that the blog title is set on init."""
        self.assertEqual("Test", self.blog.title)

    def test_blog_author_is_set(self) -> None:
        """Asserts that the blog author is set on init."""
        self.assertEqual("Test Author", self.blog.author)

    def test_blog_posts_initially_empty(self) -> None:
        """Asserts that posts list is empty on init."""
        self.assertEqual([], self.blog.posts)

    # --- __repr__ ---

    def test_repr_when_zero_posts(self) -> None:
        """Asserts __repr__ format with zero posts."""
        self.assertEqual("Test by Test Author (0 posts)", repr(self.blog))

    def test_repr_when_zero_posts_other_blog(self) -> None:
        """Asserts __repr__ on a different blog instance with zero posts."""
        blog2 = Blog("My day", "Rolf")
        self.assertEqual("My day by Rolf (0 posts)", repr(blog2))

    def test_repr_when_one_post(self) -> None:
        """Asserts __repr__ after adding one post."""
        self.blog.create_post("t1", "c1")
        self.assertEqual("Test by Test Author (1 posts)", repr(self.blog))

    def test_repr_when_two_posts(self) -> None:
        """Asserts __repr__ after adding two posts."""
        blog2 = Blog("My day", "Rolf")
        blog2.create_post("t1", "c1")
        blog2.create_post("t2", "c2")
        self.assertEqual("My day by Rolf (2 posts)", repr(blog2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
