from django.shortcuts import render

from .models import Bookmark

# 1. 목록 뷰 만들기 - ListView
# ListView 를 상속해서 BookmarkListView를 만든다
# ListView 는 쟝고에 이미 있는 기능으로 가져다 쓰는것.

from django.views.generic.list import ListView

class BookmarkListView(ListView):
        model = Bookmark
        paginate_by = 5 # 북마크 기능, 한페이지의 출력값을 결정

# 2. 북마크 상세 페이지 만들기 - DetailView
from django.views.generic.detail import DetailView

class BookmarkDetailView(DetailView):
        model = Bookmark

# 3. 북마크 추가 기능 만들기 - CreateView

from django.views.generic.edit import CreateView
from django.urls import  reverse_lazy

class BookmarkCreateView(CreateView):
        model = Bookmark
        fields = ['site_name', 'url']
        success_url = reverse_lazy('list') #success_url : 글쓰기를 완료하고 이동할 페이지
        template_name_suffix = '_create'
        # template_name_suffix : 사용할 템플릿의 접미사만 변경하는 설정값
        # 모델명_create(bookmark_create)라는 이름의 템플릿 파일을 사용하도록 설정함.

