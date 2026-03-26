from django.http import HttpResponse
from django.shortcuts import render  # 新增：导入渲染模板的函数

def index(request):
    return render(request, 'index.html')  # 正确：渲染模板并返回

def hello(request):
    views_name = '菜鸟Python教程'
    views_list = ["菜鸟教程1","菜鸟教程2","菜鸟教程3"]
    return render(request, 'index.html',{ "name":views_name ,"views_list":views_list } )
# Create your views here.
