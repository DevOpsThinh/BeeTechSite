"""
A modern blog web app

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

from atexit import register
import emoji
from django.template import Library, loader

register = Library()

@register.filter(name="comment_post_processor")
def comment_post_processor(value): 
    return emoji.emojize(value, use_aliases=True)