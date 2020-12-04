import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),  # Blog
    path("instagram/", include("instagram.urls")),  # Instagram
    # path("", TemplateView.as_view(template_name="root.html")),
    path("", RedirectView.as_view(url="/blog")),  # TODO: URL Reverse를 적용해야 합니다.
    path("__debug__/", include(debug_toolbar.urls)),
]