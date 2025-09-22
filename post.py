"""
Defines a minimal `Post` data object used to represent blog posts or articles.

The module provides a lightweight container with a JSON-friendly representation
suitable for serialization, API responses, or test fixtures.

Example:
    >>> p = Post(title="Hello", content="World")
    >>> p.json()
    {'title': 'Hello', 'content': 'World'}
"""

__author__ = 'Mihail Mihaylov'

from typing import Dict


class Post:
    """Represents a blog post with a title and content."""

    def __init__(self, title: str, content: str) -> None:
        """
        Initializes a new Post instance.

        :param title: The human-readable title of the post.
        :param content: The textual body of the post.
        """
        self.title: str = title
        self.content: str = content

    def json(self) -> Dict[str, str]:
        """
        Returns a JSON-serializable representation of the post.

        :return: Dictionary with keys 'title' and 'content'.
        """
        return {'title': self.title, 'content': self.content}
