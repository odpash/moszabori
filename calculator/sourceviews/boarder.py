from django.shortcuts import render
from django.contrib import messages
from calculator.sourcemodels.boarder import *
from calculator.sourceviews import rashet


def main(request):
    template = 'calculator/boarder.html'

    args = {
        "BoarderdlinaZabora": BoarderdlinaZabora.objects.all().values(),
        "BoardervisotaZabora": BoardervisotaZabora.objects.all().values(),
        "Boarderpaneli": Boarderpaneli.objects.all().values(),
        "Boarderrazmer": Boarderrazmer.objects.all().values(),
        "Boardermethodstand": Boardermethodstand.objects.all().values(),
        "BoarderkalitkaStandart": BoarderkalitkaStandart.objects.all().values(),
        "Boarderraspashvorota": Boarderraspashvorota.objects.all().values(),
        "Boarderotkat": Boarderotkat.objects.all().values(),
        "BoarderkmMkad": BoarderkmMkad.objects.all().values(),
        "Boarderdemontash": Boarderdemontash.objects.all().values(),
    }
    descrs = {
        "BoarderdlinaZabora": "Общая длина забора, включая ворота и калитки, м",
        "BoardervisotaZabora": "Высота забора",
        "Boarderpaneli": "Панели 3D (ячейка 200*55 мм)",
        "Boarderrazmer": "Размер столбов, мм",
        "Boardermethodstand": "Покрытие столбов",
        "BoarderkalitkaStandart": "Калитка Стандарт",
        "Boarderraspashvorota": "Распашные ворота",
        "Boarderotkat": "Откатные (сдвижные) ворота ",
        "BoarderkmMkad": "Количество км от МКАД",
        "Boarderdemontash": "Демонтаж старого забора",
    }
    data = request.GET.dict()
    if len(data) != 0:  # used after btn calculate
        for key in data.keys():
            if data[key] == '' or float(data['dlinaZabora']) <= 0 or float(data['kmMkad']) < 0:  # validator
                messages.info(request, "Расчет не был произведен!")
                messages.info(request, 'Проверьте, пожалуйста, все поля должны быть заполнены корректно.')
                return render(request, template, args)

        # here
        args = rashet.main(args, data, 'Boarder', descrs)
    return render(request, template, args)  # used at first page load
