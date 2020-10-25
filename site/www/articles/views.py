from django.shortcuts import render
from .markdown import read_markdown
import os

ARTICLES_DIR = "/var/articles"

def absolute_markdown(markdown_filename):
    abs_markdown_file = os.path.join(ARTICLES_DIR, markdown_filename)
    if os.path.isfile(abs_markdown_file):
        return abs_markdown_file
    elif os.path.isdir(abs_markdown_file):
        md_readme = os.path.join(abs_markdown_file, "README.md")
        return md_readme
    raise ValueError("Invalid File")


def articles_home(request, filename="README.md"):
    abs_markdown_file = absolute_markdown(filename)
    markdown_html = read_markdown(abs_markdown_file)
    context = {
            "article" : markdown_html,
            }
    return render(request, "articles/homepage.html", context=context)
