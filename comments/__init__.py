"""
A modern blog web app

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

def get_model():
    from django_comments.models import Comment
    return Comment

def get_form():
    from .forms import CommentForm
    return CommentForm