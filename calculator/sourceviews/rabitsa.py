from django.shortcuts import render
from calculator.sourcemodels.rabiza import *


def correct_output(arr, v):
    for i in range(len(arr)):
        if arr[i] == v:
            arr.insert(0, arr[i])
            del arr[i + 1]
            return arr


def default_values(state, arr):
    visota_arr = [float(i[0]) for i in Rabizakalitka.objects.all().values_list('visota')]
    tolshina_arr = list(set(float(i[0]) for i in Rabizadlinastolbov.objects.all().values_list('tolshina')))
    tolshinasetka_arr = list(set(float(i[0]) for i in Rabizasetka.objects.all().values_list('tolshina')))
    shirinavorot_arr = list(set(float(i[0]) for i in Rabizavorota.objects.all().values_list('shirina')))
    pokraska_arr = list(set(str(i[0]) for i in Rabizapokraska.objects.all().values_list('tip')))
    visota_arr.sort()
    tolshina_arr.sort()
    tolshinasetka_arr.sort()
    shirinavorot_arr.sort()
    kolvo_kalitok = [0, 1, 2, 3, 4, 5]
    kolvo_vorot = [0, 1, 2, 3, 4, 5]
    armatura = ["Без протяжки", 'Один ряд', "Два ряда"]
    kmMkad = 0
    dlinaZabora = 100
    if state:
        visota_arr = correct_output(visota_arr, arr[0])
        dlinaZabora = str(arr[1])
        tolshina_arr = correct_output(tolshina_arr, arr[2])
        kolvo_kalitok = correct_output(kolvo_kalitok, arr[3])
        kolvo_vorot = correct_output(kolvo_vorot, arr[4])
        shirinavorot_arr = correct_output(shirinavorot_arr, arr[5])
        tolshinasetka_arr = correct_output(tolshinasetka_arr, arr[6])
        pokraska_arr = correct_output(pokraska_arr, arr[7])
        armatura = correct_output(armatura, arr[8])

    args = {
        'dlinaZabora': dlinaZabora,
        'Rabizavisotazabora': visota_arr,
        'Rabizatolshinastolba': tolshina_arr,
        'Rabizasetka': tolshinasetka_arr,
        'Rabizakolvovorot': kolvo_vorot,
        'Rabizashirinavorot': shirinavorot_arr,
        'Rabizakolvokalitok': kolvo_kalitok,
        'Rabizapokraska': pokraska_arr,
        'Rabizaarmatura': armatura,
        'result_items': [],
        "result_ysl": [],
        "result_dos": [],
        "result_items_a": [],
        "result": 0,
        'status': 0,
        'kmMkad': kmMkad
    }
    return args


def main(request):
    template = 'calculator/rabitsa.html'
    args = default_values(False, [])
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
        args = default_values(True,
                              [visotazabora, dlinazabora, tolshinastolba, kolvo_kalitok, kolvo_vorot, shirina_vorot,
                               tolshinasetki, pokraska, armatura])
        args['status'] = 1
        count = 0
        for i in Rabizadlinastolbov.objects.all():  # ЦЕНА СТОЛБОВ
            if visotazabora == float(i.visota) and float(i.tolshina) == tolshinastolba:
                count = int((dlinazabora - kolvo_vorot * shirina_vorot - kolvo_kalitok) / 2.5 + 1)

                if count == 0:
                    continue

                args['result'] += count * float(i.price)
                args['result_items'].append(
                    {'text': f'Столб 60x30 толщиной {tolshinastolba} мм высотой {visotazabora + 1.2} м',
                     'cost': str(round(count * float(i.price), 2)),
                     'count': str(int(count)),
                     'ed': 'шт.',
                     'price': str(round(i.price, 2))
                     })

        for i in Rabizasetka.objects.all():  # СЕТКА
            if visotazabora == float(i.visota) and float(i.tolshina) == tolshinasetki:
                if dlinazabora / 10 == 0:
                    continue
                args['result'] += dlinazabora / 10 * float(i.price)
                args['result_items'].append(
                    {'text': f'Сетка с высотой {visotazabora} м и толщиной {tolshinasetki} мм',
                     'cost': str(round(dlinazabora / 10 * float(i.price), 2)),
                     'count': str(int(dlinazabora / 10)),
                     'ed': 'рул.',
                     'price': str(round(i.price, 2))
                     })

        for i in Rabizavorota.objects.all():  # ВОРОТА
            if float(i.shirina) == shirina_vorot and float(i.visota) == visotazabora:
                if kolvo_vorot == 0:
                    continue
                args['result'] += kolvo_vorot * float(i.price)
                args['result_items'].append({'text': f'Ворота {shirina_vorot}x{visotazabora} мм',
                                             'cost': str(round(kolvo_vorot * float(i.price), 2)),
                                             'count': str(int(kolvo_vorot)),
                                             'ed': 'шт.',
                                             'price': str(round(i.price, 2))
                                             })

        for i in Rabizakalitka.objects.all():  # Калитки
            if float(i.visota) == visotazabora:
                if kolvo_kalitok == 0:
                    continue
                args['result'] += kolvo_kalitok * float(i.price)
                args['result_items'].append({'text': f'Калитка {1000}x{visotazabora} мм на 1-м столбе',
                                             'cost': str(round(kolvo_kalitok * float(i.price), 2)),
                                             'count': str(int(kolvo_kalitok)),
                                             'ed': 'шт.',
                                             'price': str(round(i.price, 2))
                                             })

        if armatura == "Один ряд":
            mnosh = 1
        elif armatura == "Два ряда":
            mnosh = 2
        else:
            mnosh = 0

        for i in Rabizapokraska.objects.all():  # Покраска
            if i.tip == pokraska:
                if count * float(i.kolvo) == 0:
                    continue
                args['result'] += (dlinazabora * 0.4 + mnosh * dlinazabora) * 1.2 * float(i.price)
                args['result_items'].append(
                    {'text': f'{i.tip}',
                     'cost': str(round((dlinazabora * 0.4 + mnosh * dlinazabora) * 1.2 * float(i.price), 2)),
                     'count': str(int((dlinazabora * 0.4 + mnosh * dlinazabora) * 1.2)),
                     'ed': 'п.м.',
                     'price': str(round(i.price, 2))
                     })

                # АРМАТУРА

        armatura_price = float(Rabizaarmatura.objects.all()[0].price)
        args['result'] += dlinazabora * mnosh * armatura_price
        if dlinazabora * mnosh != 0:
            args['result_items'].append(
                {'text': f'Арматура толщиной 10 мм',
                 'cost': str(round(dlinazabora * mnosh * float(armatura_price), 2)),
                 'count': str(int(mnosh * dlinazabora)),
                 'ed': 'п.м.',
                 'price': str(round(armatura_price, 2))
                 })
            args['result_items'].append({
                'text': "Скидка 2% от стоимости материала", 'cost': str(round(args['result'] * 0.02, 2))
            })
        args['result'] *= 0.98
        args['result_items_a'] = [{
            'text': "Итого за материалы:", 'cost': str(round(args['result'], 2))
        }]
        materiali_price = args['result']
        ystanovkakalitki_price = float(Rabizaystanovkakalitki.objects.all()[0].price)
        ystanovkavorot_price = float(Rabizaystanovkavorot.objects.all()[0].price)

        args['result'] += 150 * dlinazabora / 10  # Установка сетки
        args['result_ysl'].append(
            {'text': f'Установка забора из сетки рабицы',
             'cost': str(round(150 * dlinazabora / 10, 2)),
             'count': str(int(dlinazabora / 10)),
             'ed': 'п.м.',
             'price': str(round(150, 2))
             })

        if dlinazabora * mnosh != 0:
            args['result'] += dlinazabora * mnosh * 100
            args['result_ysl'].append(
                {'text': f'Протяжка арматуры',
                 'cost': str(round(dlinazabora * mnosh * 100, 2)),
                 'count': str(int(dlinazabora * mnosh)),
                 'ed': 'п.м.',
                 'price': str(round(100, 2))
                 })

        if kolvo_vorot != 0:
            args['result'] += ystanovkavorot_price * kolvo_vorot
            args['result_ysl'].append(
                {'text': f'Установка ворот',
                 'cost': str(round(ystanovkavorot_price * kolvo_vorot, 2)),
                 'count': str(int(kolvo_vorot)),
                 'ed': 'шт.',
                 'price': str(round(ystanovkavorot_price, 2))
                 })

        if kolvo_kalitok != 0:
            args['result'] += ystanovkakalitki_price * kolvo_kalitok
            args['result_ysl'].append(
                {'text': f'Установка калитки',
                 'cost': str(round(ystanovkakalitki_price * kolvo_kalitok, 2)),
                 'count': str(int(kolvo_kalitok)),
                 'ed': 'шт.',
                 'price': str(round(ystanovkakalitki_price, 2))
                 })


        args['result_ysl_a'] = [{
            'text': "Итого за услуги:", 'cost': str(round(args['result'] - materiali_price, 2))
        }]

        kmmkad = int(float(request.GET.get('kmMkad')))
        dostavka = 0
        if 0 < kmmkad <= 5:
            dostavka += 2000
        elif 5 < kmmkad <= 25:
            dostavka += 3000
        elif kmmkad > 25:
            dostavka += 3000 + (kmmkad - 25) * 50
        args['kmMkad'] = kmmkad

        args['result'] += dostavka
        args['result_dos'].append(
            {'text': f'Доставка до участка',
             'cost': str(round(dostavka, 2)),
             'count': str(int(round(kmmkad, 2))) + " км"
             })

    args['result'] = str(round(args['result'], 2))

    for i in range(len(args['result_items'])):
        args['result_items'][i]['id'] = i + 1

    for i in range(len(args['result_ysl'])):
        args['result_ysl'][i]['id'] = i + 1

    return render(request, template, args)  # used at first page load
