from django.urls import path, re_path
from .views import index, post_detail, dynamic_image

urlpatterns = [
    path("", index),  # 최상위 주소를 뜻한다.
    # path("<int:pk>/", post_detail),
    re_path(r"^(?P<pk>\d+)/$", post_detail),
    path("dynamic_image/", dynamic_image),
    # re_path(r"^archives/(?P<year>\d{4})/$", post_archives_year),
]
