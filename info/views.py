from django.shortcuts import render


def info_views(request):
    return render(render, 'info/info.html')
