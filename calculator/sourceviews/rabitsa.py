from django.shortcuts import render
from django.contrib import messages
from calculator.sourcemodels.rabiza import *
from calculator.sourceviews import rashet


def main(request):
    args = {
        "Rabizadlinazabora": Rabizadlinazabora.objects.all().values(),
        "Rabizavisotazabora": Rabizavisotazabora.objects.all().values(),
        "Rabizamethodystanovkistolbov": Rabizamethodystanovkistolbov.objects.all().values(),
        "Rabizarazmertolshinastolb": Rabizarazmertolshinastolb.objects.all().values(),
        "Rabizapokraskastolb": Rabizapokraskastolb.objects.all().values(),
        "Rabizaraspashnievorota": Rabizaraspashnievorota.objects.all().values(),
        "Rabizakalitkastandart": Rabizakalitkastandart.objects.all().values(),
        "Rabizashirinavorot": Rabizashirinavorot.objects.all().values(),
        "Rabizademontashvorot": Rabizademontashvorot.objects.all().values(),
        "Rabizakmmkad": Rabizakmmkad.objects.all().values(),
    }
    descrs = {
        "Rabizadlinazabora": "Длина забора",
        "Rabizavisotazabora": "Высота забора",
        "Rabizamethodystanovkistolbov": "Установка стобов",
        "Rabizarazmertolshinastolb": "Размер и тощина стобов",
        "Rabizapokraskastolb": "Покраска столбов и секций",
        "Rabizaraspashnievorota": "Распашные ворота",
        "Rabizakalitkastandart": "Калитка стандарт",
        "Rabizashirinavorot": "Ширина ворот",
        "Rabizademontashvorot": "Демонтаж старого забора",
        "Rabizakmmkad": "Количество км от МКАД",
    }

    template = 'calculator/rabitsa.html'
    data = request.GET.dict()
    if len(data) != 0:  # used after btn calculate
        for key in data.keys():
            if data[key] == '' or float(data['dlinaZabora']) <= 0 or float(data['kmMkad']) < 0:  # validator
                messages.info(request, "Расчет не был произведен!")
                messages.info(request, 'Проверьте, пожалуйста, все поля должны быть заполнены корректно.')
                return render(request, template, args)

        # here
        args = rashet.main(args, data, 'Rabiza', descrs)
    return render(request, template, args)  # used at first page load
