# 21122924 刘育杰 智能科学与技术
import time

from django.shortcuts import render,HttpResponse

# 函数 Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        if username == "root" and password == "12345":
            time.sleep(1.5)
            return render(request,"choose.html")
        else:
            return render(request,"login.html")


def choose(request):
    if request.method == "GET":
        return render(request,"choose.html")


def shengxiao(request):
    return render(request,"shengxiao.html")


def jieqi(request):
    return render(request,"jieqi.html")
