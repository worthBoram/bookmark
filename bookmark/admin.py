from django.contrib import admin

# 모델을 이용한 데이터 작업을 하려면 해당 뷰를 만들어야 한다,
# 하지만 뷰를 만들기 위해 시간이 걸리고, 확인작업 때 미리 입력된 데이터가 필요하므로
# 관리자 페이지에서 미리 모델을 관리할 수 있도록 등록작업을 해둔다

from .models import Bookmark # model.py 파일에서 Bookmark 라는 모델을 불러온다.

admin.site.register(Bookmark) # 위 코드에서 불러온 모델을 해당 구문을 통해 등록