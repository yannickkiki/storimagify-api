import time

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class CsrfExemptMixin:

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UploadView(CsrfExemptMixin, View):

    @staticmethod
    def post(request):
        uploaded_files_urls = dict()
        for key, file in request.FILES.items():
            fs = FileSystemStorage()
            time_uid = int(time.time() * 1000)  # time in ms
            filename = fs.save(name=f"{time_uid}_{file.name}", content=file)
            uploaded_files_urls[key] = fs.url(filename)
        return JsonResponse(data=uploaded_files_urls)
