from django.http import Http404
from django.shortcuts import render
from articles.markdown import DjangoMarkdown, read_markdown
import os

APP_DIRECTORY = os.path.dirname(__file__)
MARKDOWN_DIR = "markdown_templates"
ALLOWED_PAGE = ['about', 'contact', "introduction"]

def absolute_markdown(markdown_filename):
    markdown_filename = os.path.join(MARKDOWN_DIR, markdown_filename)
    return os.path.join(APP_DIRECTORY, markdown_filename)

def homepage(request, pagename="introduction"):
    #Convert markdown file into html
    markdown_file = absolute_markdown(pagename + ".md")
    markdown_html = read_markdown(markdown_file)

    #Convert introduction markdwon into html
    context = {
            "article" : markdown_html,
            }
    return render(request, "home/homepage.html", context=context)
