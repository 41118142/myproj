from django.contrib import admin
from django.urls import path
from mynewapp import views  # 引入你建立的應用程式的 views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # 將首頁路徑指向 views.py 的 index 函式
]
