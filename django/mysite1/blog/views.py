from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post

# index = ListView.as_view(model=Post)


def index(request):
    post_qs = Post.objects.filter(
        status=Post.Status.PUBLISHED,
    )

    response = render(request, "blog/post_list.html", {"post_list": post_qs})

    return response


post_detail = DetailView.as_view(model=Post)


# def post_detail(request):
#     post_qs = Post.objects.filter(
#         status=Post.Status.PUBLISHED,
#     )
#     post = get_object_or_404(post_qs, pk=pk)
#     return render(request, "blog/post_detail.html", {"post": post})


# 함수 기반 뷰 (Function Based View, FBV)
# def index(request):
#     # return HttpResponse("Hello World")
#     return render(request, "blog/index.html")


# 클래스 기반 뷰 (Class Based View, CBV) -> 정적인 설정만 있을 때
# index = TemplateView.as_view(template_name="blog/index.html")


# class IndexView(TemplateView):
#     template_name = "blog/index.html"


# index = IndexView.as_view()


# def make_index_view():
#     def view(request):
#         return HttpResponse("hello")

#     return view


# index = make_index_view()
