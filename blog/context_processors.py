"""
A modern blog web app

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

from wagtail.core.models import Site
from blog.models import BlogPage

def blog_page(request):
    bee_site = Site.find_for_request(request)
    context = {
        "blog_page": BlogPage.objects.in_site(bee_site).first()
    }
    return context