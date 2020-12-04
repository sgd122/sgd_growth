from django.urls import path, re_path, register_converter
from .views import index, post_detail, dynamic_image, archives_by_year
from blog.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("", index),  # 최상위 주소를 뜻한다.
    path("<int:pk>/", post_detail),
    path("dynamic_image/", dynamic_image),
    # re_path(r"^(?P<pk>\d+)/$", post_detail),
    path("archives/<yyyy:year>/", archives_by_year),
    # re_path(r"^archives/(?P<year>\d{4})/$", archives_by_year),
    # re_path(r'^(?P<pk>\d+)/$', post_detail),
    # re_path(r'^(?P<pk>\d+)/excel/$', post_download),
]
