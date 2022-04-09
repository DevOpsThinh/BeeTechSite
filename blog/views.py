"""
A modern blog web app

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from wagtail.core.models import Site

# Create your views here.

class RobotsView(TemplateView):
    content_type = "text/plain"
    template_name = "robots.txt"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = context["view"].request
        context["bee_site"] = Site.find_for_request(request)
        return context