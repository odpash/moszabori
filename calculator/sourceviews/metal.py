from django.shortcuts import render
from django.contrib import messages

from calculator.sourceviews import rashet
from calculator.sourcemodels.metal import *


def main(request):
    template = 'calculator/metal.html'

    descrs = {
        "MetaldlinaZabora": "Длина забора",
        "MetalvisotaZabora": "Высота забора",
        "Metaltipshtaketnik": "Штакетник",
        "Metalkreplenieshtaketnik": "Крепление",
        "Metalzazor": "Зазор",
        "Metalpokritiestaketnik": "Покрытие",
        "Metalkolvoryadlag": "Количество рядов",
        "Metalmetodystanovki": "Метод установки",
        "Metalrazmer": "Размер и толщина столбцов",
        "Metalshag": "Шаг между столбами",
        "Metalpaint": "Покраска",
        "Metalstandart": "Калитка Стандарт",
        "Metalraspash": "Распашные ворота",
        "Metalotkat": "Откатные (сдвижные) ворота",
        "Metaldetektprotekt": "Защитная декоративная планка",
        "Metaldemontash": "Демонтаж старого забора",
        "MetalkmMkad": "Расстояние от МКАД",
    }
    args = {
        'MetaldlinaZabora': MetaldlinaZabora.objects.all().values(),
        'MetalvisotaZabora': MetalvisotaZabora.objects.all().values(),
        'Metaltipshtaketnik': Metaltipshtaketnik.objects.all().values(),
        'Metalkreplenieshtaketnik': Metalkreplenieshtaketnik.objects.all().values(),
        'Metalzazor': Metalzazor.objects.all().values(),
        'Metalpokritiestaketnik': Metalpokritiestaketnik.objects.all().values(),
        'Metalkolvoryadlag': Metalkolvoryadlag.objects.all().values(),
        'Metalmetodystanovki': Metalmetodystanovki.objects.all().values(),
        'Metalrazmer': Metalrazmer.objects.all().values(),
        'Metalshag': Metalshag.objects.all().values(),
        'Metalpaint': Metalpaint.objects.all().values(),
        'Metalstandart': Metalstandart.objects.all().values(),
        'Metalraspash': Metalraspash.objects.all().values(),
        'Metalotkat': Metalotkat.objects.all().values(),
        'Metaldetektprotekt': Metaldetektprotekt.objects.all().values(),
        'Metaldemontash': Metaldemontash.objects.all().values(),
        'MetalkmMkad': MetalkmMkad.objects.all().values(),

    }
    data = request.GET.dict()
    if len(data) != 0:  # used after btn calculate
        for key in data.keys():
            if data[key] == '' or float(data['dlinaZabora']) <= 0 or float(data['kmMkad']) < 0:  # validator
                messages.info(request, "Расчет не был произведен!")
                messages.info(request, 'Проверьте, пожалуйста, все поля должны быть заполнены корректно.')
                return render(request, template, args)

        # here
        args = rashet.main(args, data, 'Metal', descrs)
    return render(request, template, args)  # used at first page load
