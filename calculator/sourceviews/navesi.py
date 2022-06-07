from django.shortcuts import render


def main(request):

    template = 'calculator/navesi.html'
    return render(request, template)
