from django.shortcuts import render

def gotomusic(request):
    return render(request, 'home/musichome.html')

