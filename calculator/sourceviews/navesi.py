from django.shortcuts import render
from django.contrib import messages

from calculator.sourceviews.rasheti import navesi
from calculator.sourcemodels.navesi import *


def main(request):
    template = 'calculator/navesi.html'
    args = {
        "NavesidlinaZabora": NavesidlinaZabora.objects.all().values(),
        "NavesishirinaZabora": NavesishirinaZabora.objects.all().values(),
        "NavesivisotaZabora": NavesivisotaZabora.objects.all().values(),
        "Navesityp": Navesityp.objects.all().values(),
        "Navesirazmer": Navesirazmer.objects.all().values(),
        "Navesimethod": Navesimethod.objects.all().values(),
        "Navesikrovlya": Navesikrovlya.objects.all().values(),
        "Navesifermi": Navesifermi.objects.all().values(),
        "NavesiMetalkmMkad": NavesikmMkad.objects.all().values(),
    }
    data = request.GET.dict()
    if len(data) != 0:  # used after btn calculate
        for key in data.keys():
            if data[key] == '' or float(data['dlinaZabora']) <= 0 or float(data['shirinaZabora']) <= 0 or float(data['kmMkad']) < 0:  # validator
                messages.info(request, "Расчет не был произведен!")
                messages.info(request, 'Проверьте, пожалуйста, все поля должны быть заполнены корректно.')
                return render(request, template, args)

        # here
        args = navesi.main(args, data)
    return render(request, template, args)  # used at first page load
