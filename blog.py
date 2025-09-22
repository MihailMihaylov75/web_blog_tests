"""
Simple blog domain model: a Blog that aggregates Post objects.

The Blog stores a title, an author, and a list of posts. It can create new posts
and provide a JSON-serializable representation suitable for APIs or fixtures.

Example:
    >>> b = Blog(title="Tech Notes", author="Mihail")
    >>> b.create_post(title="Hello", content="World")
    >>> len(b.posts)
    1
    >>> b.json()["title"]
    'Tech Notes'
"""

from __future__ import annotations

__author__ = "Mihail Mihaylov"

from typing import List

from post import Post


class Blog:
    """Represents a blog with metadata and a collection of posts."""

    def __init__(self, title: str, author: str) -> None:
        """
        Initializes a new Blog instance.

        :param title: The title of the blog.
        :param author: The display name of the blog author.
        """
        self.title: str = title
        self.author: str = author
        self.posts: List[Post] = []

    def __repr__(self) -> str:
        """
        Returns a human-readable representation of the blog.

        :return: String in the format '<title> by <author> (<N> posts)'.
        """
        return f"{self.title} by {self.author} ({len(self.posts)} posts)"

    def create_post(self, title: str, content: str) -> None:
        """
        Creates and appends a new post to the blog.

        :param title: Post title.
        :param content: Post body content.
        """
        self.posts.append(Post(title=title, content=content))

    def json(self) -> dict:
        """
        Returns a JSON-serializable representation of the blog.

        :return: Dictionary with keys 'title', 'author', and 'posts'.
        """
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }
