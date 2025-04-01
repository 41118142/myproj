from django.http import HttpResponse  # 確認這行存在

# 建立一個簡單的視圖函式
def index(request):
    return HttpResponse("<h1>學號：41118142<br>姓名：林宸宇</h1>")
