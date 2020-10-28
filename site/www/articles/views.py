from django.shortcuts import render
from .markdown import read_markdown
from .forms import CommentaryForm
from .models import Commentary
import os

import sys

ARTICLES_DIR = "/var/articles"

def absolute_markdown(markdown_filename):
    """
    Retrieve absolute path of an article file, written in markdown.
    Could an article, or a folder of articles. In the last case,
    return README.md of the folder.
    """
    abs_markdown_file = os.path.join(ARTICLES_DIR, markdown_filename)
    if os.path.isfile(abs_markdown_file + ".md"):
        return abs_markdown_file + ".md"
    elif os.path.isdir(abs_markdown_file):
        md_readme = os.path.join(abs_markdown_file, "README.md")
        return md_readme
    raise ValueError("Invalid File : {}".format(abs_markdown_file))

def post_comment(request):
    """
    Save posted comment related to an article.
    """
    post_context = {}
    commentary_form = CommentaryForm(request.POST)
    
    #Register Commentary
    if commentary_form.is_valid():
        commentary_form.cleaned_data.pop("captcha")
        comment = Commentary(**commentary_form.cleaned_data, \
                article=request.POST['article'])
        comment.save()
        post_context['anchor'] = comment.id

    #On form error, prepopulate Form with sended data
    else:
        error_form = CommentaryForm({
            "username" : request.POST['username'],
            "comment" : request.POST['comment']})
        post_context['anchor'] = "post-comment"
        post_context['form'] = error_form
        post_context['error_message'] = \
                "Formulaire invalide, vérifier le captcha"

    return post_context

def articles_home(request, filename=""):
    """
    Main view to render all articles.
    URLs will represent an article filename without extension,
    or a folder of articles.

    Serve `Culture-numerique/articles` folder under '/articles/'.
    """
    #Allow comment if it's not article homepage (/articles/)
    allow_comment = filename != ""

    #If comment have been posted
    if request.POST:
        post_context = post_comment(request)

    #Find (markdown) article related to url
    abs_markdown_file = absolute_markdown(filename)
    markdown_html = read_markdown(abs_markdown_file)
    context = {
            "article_file" : filename,
            "article_content" : markdown_html,
            "form" : CommentaryForm(), 
            "allow_comment" : allow_comment,
            }

    #Extra context if POST request
    if locals().get("post_context"):
        context.update(post_context)

    if allow_comment:
        context['comments'] = Commentary.objects.filter(article=filename)
    return render(request, "articles/homepage.html", context=context)
