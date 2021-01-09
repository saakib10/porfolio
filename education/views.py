from django.shortcuts import render

def education_show(request):
    context = {'education':'active'}
    return render(request,'edu.html',context)
