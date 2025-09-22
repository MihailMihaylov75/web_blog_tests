"""
Console UI for a minimal Blog application.

The module exposes a simple command-line menu that lets a user:
- create blogs
- list available blogs
- read a specific blog and its posts
- create a post in a blog

Example flow:
    > Enter "c" to create a blog, "l" to list them, "r" to read one, "p" to write a post, or "q" to quit:
    c
    Please enter a blog title: Tech Notes
    Please enter your name: Mihail
    l
    - Tech Notes by Mihail (0 posts)
    p
    Enter the blog title you want to create a post in: Tech Notes
    Enter your post title: Hello
    Enter your post content: World
    r
    Enter a blog title you want to read: Tech Notes
    ---Hello---

    World
"""

from __future__ import annotations

__author__ = "Mihail Mihaylov"

from typing import Dict

from blog import Blog

MENU_PROMPT: str = (
    'Enter "c" to create a blog, "l" to list them, "r" to read one, '
    '"p" to write a post, or "q" to quit: '
)

POST_TEMPLATE: str = """
---{}---

{}
"""

blogs: Dict[str, Blog] = {}


def menu() -> None:
    """
    Runs the main interactive menu loop.

    :return: None.
    """
    print_blogs()

    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs() -> None:
    """
    Prints all blogs in the global registry.

    :return: None.
    """
    for _, blog in blogs.items():
        print(f"- {blog}")


def ask_create_blog() -> None:
    """
    Prompts the user for blog metadata and creates a new Blog.

    :return: None.
    """
    title = input("Please enter a blog title: ")
    author = input("Please enter your name: ")
    blogs[title] = Blog(title=title, author=author)


def ask_read_blog() -> None:
    """
    Prompts for a blog title and prints all posts of that blog.

    If the blog does not exist, prints a warning and returns.

    :return: None.
    """
    title = input("Enter a blog title you want to read: ")
    blog = blogs.get(title)
    if not blog:
        print(f'No blog found with title "{title}".')
        return

    print_posts(blog)


def print_posts(blog: Blog) -> None:
    """
    Prints all posts for a given Blog.

    :param blog: Blog instance whose posts will be printed.
    :return: None.
    """
    for post in blog.posts:
        print_post(post.title, post.content)


def print_post(title: str, content: str) -> None:
    """
    Prints a single post using the predefined template.

    :param title: Post title.
    :param content: Post content/body.
    :return: None.
    """
    print(POST_TEMPLATE.format(title, content))


def ask_create_post() -> None:
    """
    Prompts for a target blog and post data, then creates the post.

    If the blog does not exist, prints a warning and returns.

    :return: None.
    """
    blog_title = input("Enter the blog title you want to create a post in: ")
    blog = blogs.get(blog_title)
    if not blog:
        print(f'No blog found with title "{blog_title}".')
        return

    title = input("Enter your post title: ")
    content = input("Enter your post content: ")
    blog.create_post(title=title, content=content)


if __name__ == "__main__":
    menu()
