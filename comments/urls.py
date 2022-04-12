"""
Custom Comments

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

from django.urls import include, path
from .views import mention_query

urlpatterns = [
    path('mention/', mention_query, name="comments-mention-query"),
    path('', include('django_comments.urls')),
]