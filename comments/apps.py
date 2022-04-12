"""
A modern blog web app

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

from django.apps import AppConfig


class CustomCommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'

    def ready(self):
        import comments.receivers
