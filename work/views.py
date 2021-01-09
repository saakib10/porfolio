from django.shortcuts import render

def work_show(request):
    context = {'work':'active'}
    return render(request,'work.html',context)
