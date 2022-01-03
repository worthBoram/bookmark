from django.db import models

# Create your models here.
class Bookmark(models.Model): # 해당 자료를 데이터베이스에 저장할 수 있도록 모델 생성
    site_name = models.CharField(max_length=100) # 필드
    url = models.URLField('Site URL')

# 모델에 _str_ 메서드 추가
# 매직 메서드(던더 메서드) : 언더바가 앞뒤로 붙어있는 함수들, 클래스의 오브젝트를 출력할 때 나타날 내용을 결정하는 메서드
    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url
