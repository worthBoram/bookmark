from django.urls import path
from .views import BookmarkListView, BookmarkDetailView, BookmarkCreateView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
        # '' : bookrmark/ 이하 부분이 없다. 즉 bookmark 앱의 루트 페이지
        # BookmarkListView.as_view() : BookmarkListView 라는 뷰를 호출하겠다. (클래스 형 뷰일 경우 as_view() 를 붙여야 함)
        # name 은 설정한 이름을 가지고 해당 url 패턴을 찾을 수 있도록 하는 역햘
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
        # <int:pk> : int 는 타입, 정확히는 컨버터
        # 컨버터 종류 : str, int, slug, uuid, path
        # 뒤쪽은 컨버터를 통해 반환 받은 값 혹은 패턴에 일치하는 값의 변수명
    path('add/', BookmarkCreateView.as_view(), name='add'),
]