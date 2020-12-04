import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.http import HttpRequest, HttpResponse, response
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post

# index = ListView.as_view(
#     model=Post,
#     queryset=(Post.objects.filter(
#         status=Post.Status.PUBLISHED,
#     ))
# )


def index(request):
    # image_url = "https://images.heb.com/is/image/HEBGrocery/000320625"
    # res = requests.get(image_url)
    # image_data = res.content

    # response = HttpResponse(content_type="image/jpeg")
    # response.write(image_data)
    # response[
    #     "Content-Disposition"
    # ] = "attachment; filename=flower.jpg"  # Custom 응답 Header 지정

    # return response

    post_qs = Post.objects.filter(
        status=Post.Status.PUBLISHED,
    )

    response = render(request, "blog/post_list.html", {"post_list": post_qs})

    return response


# post_detail = DetailView.as_view(model=Post)


def post_detail(request, pk):
    post_qs = Post.objects.filter(
        status=Post.Status.PUBLISHED,
    )
    post = get_object_or_404(post_qs, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def dynamic_image(request: HttpRequest) -> HttpResponse:
    name = request.GET.get("name", "홍길동")

    # 윈도우의 맑은고딕 폰트 경로
    # 맥에서는 애플고딕 경로 -> '/Library/Fonts/AppleGothic.ttf'
    # ttf_path = 'C:/Windows/Fonts/malgun.ttf'
    ttf_path = "/Library/Fonts/AppleGothic.ttf"

    image_url = "http://www.flowermeaning.com/flower-pics/Calla-Lily-Meaning.jpg"

    res = requests.get(image_url)  # 서버로 HTTP GET 요청하여, 응답 획득
    io = BytesIO(res.content)  # 응답의 Raw Body. 메모리 파일 객체 BytesIO 인스턴스 생성
    io.seek(0)  # 파일의 처음으로 커서를 이동

    canvas = Image.open(io).convert("RGBA")  # 이미지 파일을 열고, RGBA모드로 변환

    font = ImageFont.truetype(ttf_path, 40)  # 지정 경로의 TrueType 폰트, 폰트크기 40
    draw = ImageDraw.Draw(canvas)  # canvas에 대한 ImageDraw 객체 획득

    text = name  # '홍길동'
    left, top = 10, 10
    margin = 10
    width, height = font.getsize(text)
    right = left + width + margin
    bottom = top + height + margin

    draw.rectangle((left, top, right, bottom), (255, 255, 224))
    draw.text((15, 15), text, font=font, fill=(20, 20, 20))

    response = HttpResponse(content_type="image/png")
    canvas.save(response, format="PNG")  # HttpResponse file-like 특성 활용
    return response


# -------------------------------------------- #
# -------------------------------------------- #

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
