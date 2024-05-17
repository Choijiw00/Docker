from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('', lambda request: HttpResponseRedirect('/todo/')),  # 기본 URL 리디렉션 설정
]