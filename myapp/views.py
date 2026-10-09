from django.shortcuts import render, redirect
from myapp.models import UserInfo


def info_list(request):
    data_list = UserInfo.objects.all()
    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')
    user = request.POST.get("user")
    password = request.POST.get("pwd")
    age = request.POST.get("age")
    UserInfo.objects.create(name=user, password=password, age=age or 999)
    return redirect("/info/list/")


def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")
