import markdown
from markdown.extensions import Extension
from markdown.inlinepatterns import LinkInlineProcessor, LINK_RE
from urllib.parse import urlparse

class DjangoLinkProcessor(LinkInlineProcessor):
    """
    Convert markdown internal links to django compatible
    links.
    """
    def getLink(self, data, index):
        href, *link_data = super().getLink(data, index)
        url_split = urlparse(href)

        #Perform action on internal links
        if not url_split.netloc and not url_split.scheme:
            pass
        return (href, *link_data)

class DjangoMarkdownExtension(markdown.Extension):
    def extendMarkdown(self, md, *args, **kwargs):
        md.inlinePatterns.register(DjangoLinkProcessor(LINK_RE, md), 
                "link", 160)

class DjangoMarkdown(markdown.Markdown):
    """
    Custom markdown renderer used for django,
    handle specific behavior related to the framework.
    """
    def __init__(self, *args, **kwargs):
        extensions = kwargs.get('extensions', [])
        extensions.append(DjangoMarkdownExtension())
        kwargs['extensions'] = extensions
        super().__init__(*args, **kwargs)

def read_markdown(markdown_filename):
    """
    Read a markdown file, and convert him into html.
    """
    with open(markdown_filename) as markdown_stream:
        raw_markdown = markdown_stream.read()

    md_renderer = DjangoMarkdown()
    return md_renderer.convert(raw_markdown)
