from django.http import Http404
from django.shortcuts import render
from articles.markdown import DjangoMarkdown
import os

APP_DIRECTORY = os.path.dirname(__file__)
ALLOWED_PAGE = ['articles', 'about', 'contact', "introduction"]

def read_markdown(markdown_filename):
    MARKDOWN_DIR = os.path.join(APP_DIRECTORY, "markdown_templates")
    abs_markdown_filename = os.path.join(MARKDOWN_DIR, markdown_filename)

    with open(abs_markdown_filename) as markdown_stream:
        return markdown_stream.read()

def homepage(request, pagename="introduction"):
    #Retrieve content of introduction file
    
    if pagename not in ALLOWED_PAGE:
        raise Http404("Page Not found")

    markdown_file = pagename + ".md"
    markdown_content = read_markdown(markdown_file)

    #Convert introduction markdwon into html
    md_renderer = DjangoMarkdown()
    output = md_renderer.convert(markdown_content)
    context = {
            "article" : output,
            }
    return render(request, "home/homepage.html", context=context)
