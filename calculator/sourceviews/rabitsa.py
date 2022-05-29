from django.shortcuts import render
from django.contrib import messages
from calculator.sourcemodels.rabiza import *


def default_values():
    visota_arr = [float(i[0]) for i in Rabizakalitka.objects.all().values_list('visota')]
    tolshina_arr = list(set(float(i[0]) for i in Rabizadlinastolbov.objects.all().values_list('tolshina')))
    tolshinasetka_arr = list(set(float(i[0]) for i in Rabizasetka.objects.all().values_list('tolshina')))
    shirinavorot_arr = list(set(float(i[0]) for i in Rabizavorota.objects.all().values_list('shirina')))
    pokraska_arr = list(set(str(i[0]) for i in Rabizapokraska.objects.all().values_list('tip')))
    visota_arr.sort()
    tolshina_arr.sort()
    tolshinasetka_arr.sort()
    shirinavorot_arr.sort()

    args = {
        'Rabizavisotazabora': visota_arr,
        'Rabizatolshinastolba': tolshina_arr,
        'Rabizasetka': tolshinasetka_arr,
        'Rabizakolvovorot': [0, 1, 2, 3, 4, 5],
        'Rabizashirinavorot': shirinavorot_arr,
        'Rabizakolvokalitok': [0, 1, 2, 3, 4, 5],
        'Rabizapokraska': pokraska_arr,
        'Rabizaarmatura': ["Без протяжки", 'Один ряд', "Два ряда"]
    }
    return args


def main(request):
    template = 'calculator/rabitsa.html'
    args = default_values()
    args['result_items'] = []
    args['result_ysl'] = []
    args['result_dos'] = []
    args['result'] = 0
    if request.GET.get('Rabizadlinazabora') is not None:
        visotazabora = float(str(request.GET.get('Rabizavisotazabora')).replace(',', '.'))
        dlinazabora = float(str(request.GET.get('Rabizadlinazabora')).replace(',', '.'))
        tolshinastolba = float(str(request.GET.get('Rabizatolshinastolba')).replace(',', '.'))
        kolvo_kalitok = float(str(request.GET.get('Rabizakolvokalitok')).replace(',', '.'))
        kolvo_vorot = float(str(request.GET.get('Rabizakolvovorot')).replace(',', '.'))
        shirina_vorot = float(str(request.GET.get('Rabizashirinavorot')).replace(',', '.'))
        tolshinasetki = float(str(request.GET.get('Rabizasetka')).replace(',', '.'))
        pokraska = request.GET.get('Rabizapokraska')
        armatura = request.GET.get("Rabizaarmatura")

        count = 0
        for i in Rabizadlinastolbov.objects.all():  # ЦЕНА СТОЛБОВ
            if visotazabora == float(i.visota) and float(i.tolshina) == tolshinastolba:
                count = int((dlinazabora - kolvo_vorot * shirina_vorot - kolvo_kalitok))
                print(count)
                args['result'] += count * float(i.price) / 2.5
                args['result_items'].append({'text': f'Столбы ({count / 2.5} шт.) - {i.price} рублей за столб',
                                             'cost': round(count * float(i.price) / 2.5, 2)})

        for i in Rabizasetka.objects.all():  # СЕТКА
            if visotazabora == float(i.visota) and float(i.tolshina) == tolshinasetki:
                args['result'] += visotazabora / 10 * float(i.price)
                args['result_items'].append(
                    {'text': f'Сетка ({round(visotazabora / 10, 2)} ед.) - {i.price} рублей за рулон',
                     'cost': round(visotazabora / 10 * float(i.price), 2)})

        for i in Rabizavorota.objects.all():  # ВОРОТА
            if float(i.shirina) == shirina_vorot and float(i.visota) == visotazabora:
                args['result'] += kolvo_vorot * float(i.price)
                args['result_items'].append({'text': f'Ворота ({kolvo_vorot} шт.) - {i.price} рублей за штуку',
                                             'cost': round(kolvo_vorot * float(i.price), 2)})

        for i in Rabizakalitka.objects.all():  # Калитки
            if float(i.visota) == visotazabora:
                args['result'] += kolvo_kalitok * float(i.price)
                args['result_items'].append({'text': f'Калитки ({kolvo_kalitok} шт.) - {i.price} рублей за штуку',
                                             'cost': round(kolvo_kalitok * float(i.price), 2)})

        for i in Rabizapokraska.objects.all():  # Покраска
            if i.tip == pokraska:
                args['result'] += count * float(i.kolvo) * float(i.price)
                args['result_items'].append(
                    {'text': f'{i.tip} ({round(count * float(i.kolvo), 2)} шт.) - {i.price} рублей за штуку',
                     'cost': round(count * float(i.kolvo) * float(i.price), 2)})

                # АРМАТУРА
        if armatura == "Один ряд":
            mnosh = 1
        elif armatura == "Два ряда":
            mnosh = 2
        else:
            mnosh = 0
        armatura_price = float(Rabizaarmatura.objects.all()[0].price)
        args['result'] += dlinazabora * mnosh * armatura_price
        args['result_items'].append(
            {'text': f'Арматура ({mnosh * dlinazabora} шт.) - {armatura_price} рублей за п.м.',
             'cost': round(dlinazabora * mnosh * float(armatura_price), 2)})

        ystanovkakalitki_price = float(Rabizaystanovkakalitki.objects.all()[0].price)
        ystanovkavorot_price = float(Rabizaystanovkavorot.objects.all()[0].price)
        args['result'] += ystanovkavorot_price * kolvo_vorot

        args['result_ysl'].append(
            {'text': f'Установка ворот ({kolvo_vorot} шт.) - {ystanovkavorot_price * kolvo_vorot} рублей за ворота',
             'cost': round(ystanovkavorot_price * kolvo_vorot, 2)})

        args['result'] += ystanovkakalitki_price * kolvo_kalitok
        args['result_ysl'].append(
            {'text': f'Установка калитки ({kolvo_kalitok} шт.) - {ystanovkakalitki_price * kolvo_kalitok} рублей за калитку',
             'cost': round(ystanovkakalitki_price * kolvo_kalitok, 2)})

        kmmkad = int(float(request.GET.get('kmMkad')))
        dostavka = kmmkad * 30
        if kmmkad > 30:
            kmmkad_res = kmmkad - 30
            dostavka += kmmkad_res * 65
        args['result'] += dostavka
        args['result_dos'].append(
            {'text': f'Доставка ({kmmkad} км)',
             'cost': round(dostavka, 2)})

    args['result'] = round(args['result'], 2)
    return render(request, template, args)  # used at first page load
