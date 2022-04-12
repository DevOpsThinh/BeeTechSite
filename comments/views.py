"""
Custom Views

Created by Nguyen Truong Thinh
Contact me: nguyentruongthinhvn2020@gmail.com || +84393280504
"""

from django.shortcuts import redirect
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from wagtail.admin import messages
from wagtail.contrib.modeladmin.views import DeleteView

from . import get_model as get_comment_model

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

def mention_query(request):
    content_type = request.GET.get("content_type")
    object_pk = request.GET.get("object_pk")

    app_label, model = content_type.split(".")
    content_type = ContentType.objects.get(app_label=app_label, model=model)

    comment_model = get_comment_model()

    data = comment_model.objects.filter(
        content_type=content_type, object_pk=object_pk,
    ).filter(is_removed=False).values("user_name").order_by('user_name').distinct()

    resp = {"result": list(data)}
    return JsonResponse(resp)

