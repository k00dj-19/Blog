from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects # 개체들의 목록을 전달받는 객체 = 쿼리셋
    return render(request, 'home.html', {'blogs': blogs})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드
