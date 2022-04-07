"""
Run Python markdown to render the markdown content to HTML

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

import markdown
import html

class MathJaxPattern(markdown.inlinepatterns.Pattern):

    def __init__(self, md):
        markdown.inlinepatterns.Pattern.__init__(
            self, r"(?<!\\)(\$\$?)(.+?)\2", md
        )

    def handleMatch(self, m):
        text = html.escape(m.group(2) + m.group(3) + m.group(2))
        return self.markdown.htmlStash.store(text)

class MathJaxExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add("mathjax", MathJaxPattern(md), "<escape")

def makeExtension(**kwargs):
    return MathJaxExtension(**kwargs)
