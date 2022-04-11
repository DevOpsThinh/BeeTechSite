"""
Custom Views

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

from django.shortcuts import redirect
from wagtail.admin import messages
from wagtail.contrib.modeladmin.views import DeleteView

# Create your views here.

"""
The Comment Delete View
"""
class CommentDeleteView(DeleteView):
    page_title = "Delete comment"

    def post(self, request, *args, **kwargs):
        try:
            self.instance.is_removed = True
            self.instance.save()
            mess = f"{self.verbose_name} '{self.instance}' deleted."
            messages.success(request, mess)
            return redirect(self.index_url)
        except Exception as e:
            raise e

