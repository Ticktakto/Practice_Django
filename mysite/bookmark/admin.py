from django.contrib import admin
from bookmark.models import Bookmark

# 데코레이터 (기존 함수 수정하지 않고, 추가 기능 구현 시)
# admin.register(Bookmark) 추가 기능 확장 구현
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

# Register your models here. (admin 사이트에 테이블 반영)
