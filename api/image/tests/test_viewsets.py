from rest_framework.test import APITestCase

from api.image.models import Image
from api.xlib.testcases.viewsets import ModelViewSetTestCaseMixin


class ImageViewSetTest(ModelViewSetTestCaseMixin, APITestCase):
    model = Image
    base_url = '/api/image/'
    fields = ('id', 'url')
    data_create = {'url': 'https://yannick.almeki.co/talk/silver-medal-at-acpc-benin-2019/featured_hufa3d0f4f82d253dc80545e32801731a5_73366_720x0_resize_q75_lanczos.jpeg'}
