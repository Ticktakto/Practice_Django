from django.contrib import admin
from django.urls import path

from bookmark.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # class - based view
    path('bookmark/', BookmarkLV.as_view(), name='index' ),
    path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail')
]
