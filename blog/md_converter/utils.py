"""
Run Python markdown to render the markdown content to HTML

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

import markdown

def render_markdown(value):
    html = markdown.markdown(
        value,
        extensions=[
            "extra",
            "codehilite",
            "blog.md_converter.mdx.mdx_mathjax",
        ],
        extension_configs={
            "codehilite": [
                ("guess_lang", False)
            ]
        },
        output_format="html5"
    )
    return html