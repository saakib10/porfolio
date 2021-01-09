from django.shortcuts import render

def show_skill(request):
    context = {'skill' : 'active'}
    return render(request,'skill.html',context)
