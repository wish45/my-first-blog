from django.contrib import admin
from .models import Post

admin.site.register(Post)  #관리자페이지에서 만든 모델을 보려면 이렇게 써야함.