from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# 함수 기반 뷰 (Function Based View, FBV)
# def index(request):
#     # return HttpResponse("Hello World")
#     return render(request, "blog/index.html")


# 클래스 기반 뷰 (Class Based View, CBV) -> 정적인 설정만 있을 때
# index = TemplateView.as_view(template_name="blog/index.html")


class IndexView(TemplateView):
    template_name = "blog/index.html"


index = IndexView.as_view()


def make_index_view():
    def view(request):
        return HttpResponse("hello")

    return view


# index = make_index_view()