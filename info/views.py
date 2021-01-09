from django.shortcuts import render

def info_show(request):
    context = {'info':'active'}
    return render(request,'info.html',context)
