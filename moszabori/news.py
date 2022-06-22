from django.shortcuts import render


def main(request):
    template = 'moszabori/1.html'
    return render(request, template)

