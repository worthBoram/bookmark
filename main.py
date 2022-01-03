# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# 1.프로젝트를 만들 때 마다 쟝고를 설치한다
# $ pip install django

# 2. 장고 프로젝트를 만든다
# $ django-admin startproject config .
# . 은 현재 폴더에 파일을 만들겠다는 의미. config 폴더가 생기고 manage.py 파일이 만들어진다.

# 3. 데이터베이스(DB) 생성 : db를 초기화 하면서 db 파일을 생성한다.
# $ python manage.py migrate
# db.sqlite3 파일이 생성됨

# 4. 디자인패턴 생성 ( 프로젝트에 기능 단위인 앱을 새로 만든다)
# $ python manage.py startapp 앱명칭 (띄어쓰기x _ 로 연결)

# 5. 관리자 계정 생성
# $ python manage.py createsuperuser

# 6. 서버 실행 - 사이트 돌아가는지 확인하기
# $ python manage.py runserver
# 127.0.0.1:8000 생성됨


# 7. 모델 만들기
# 7-1. 모델 만들기
# models.py 파일에 models.Model 을 상속받는 클래스 생성, 필드 생성

# 7-2. 앱을 사용하기 위한 설정 추가
# setting.py 파일에서 INSTALLED_APPS 변수 끝에 사용하고자 하는 앱의 명칭 추가
# ex. 'bookmark', -- 콤마 빼먹지 말기

# 7-3. 마이그레이션 파일 생성 명령
# $ python manage.py makemigrations bookmark : bookmark 앱에 마이그레이션 파일 생성
# 마이그레이션 파일 : 앱에서 데이터베이스 관련 변경사항이 있는지 확인하고 변경할 내용이 있다면 생성하는 파일.

# 7-4. 마이그레이션 파일 내용을 실제 데이터베이스에 적용 명령
# $ python manage.py migrate bookmark

# 8. 관리자 페이지에 모델 등록
# admin.py 에 코드 입력

# 9. 뷰 만들기

# 9-1. view.py 파일에 원하는 형태의 view 를 생성

# 9-2. URL 연결하기 : view를 호출할 수 있도록 연결한다.
# urls.py 에서 설정. config 폴더에 있는 루트파일과 각 앱 폴더에 만들어두는 서브파일이 있다.

# 9-3. 북마크 앱 폴더에 urls.py 파일을 생성하여, bookmark/ 이하 url을 어떤 뷰와 연결할지 설정해준다.

# 10. 템플릿 만들기
# templates 폴더에 위치해야 한다