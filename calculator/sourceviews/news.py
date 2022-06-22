from django.shortcuts import render


def main(request):
    return render(request, 'news/1.html')


def main2(request):
    return render(request, 'news/2.html')


def main3(request):
    return render(request, 'news/3.html')
