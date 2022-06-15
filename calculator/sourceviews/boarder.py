from django.shortcuts import render
from calculator.sourcemodels.boarder import *


def correct_output(arr, v):
    for i in range(len(arr)):
        if arr[i] == v:
            arr.insert(0, arr[i])
            del arr[i + 1]
            return arr


def default_values(state, arr):
    visota_arr = [float(i[0]) for i in Boarderkalitka.objects.all().values_list('visota')]
    tolshina_arr = list(set(float(i[0]) for i in Boarderdlinastolbov.objects.all().values_list('tolshina')))
    shirinavorot_arr = list(set(float(i[0]) for i in Boardervorota.objects.all().values_list('shirina')))
    pokraska_arr = list(set(str(i[0]) for i in Boarderpokraska.objects.all().values_list('tip')))
    panels_arr = list(set(str(i[0]) for i in Boarder3d.objects.all().values_list('title')))
    kolvo_kalitok = [0, 1, 2, 3, 4, 5]
    kolvo_vorot = [0, 1, 2, 3, 4, 5]
    kmMkad = 0
    dlinaZabora = 100
    visota_arr.sort()
    tolshina_arr.sort()
    shirinavorot_arr.sort()
    if state:
        visota_arr = correct_output(visota_arr, arr[0])
        dlinaZabora = str(arr[1])
        tolshina_arr = correct_output(tolshina_arr, arr[2])
        kolvo_kalitok = correct_output(kolvo_kalitok, arr[3])
        kolvo_vorot = correct_output(kolvo_vorot, arr[4])
        shirinavorot_arr = correct_output(shirinavorot_arr, arr[5])
        pokraska_arr = correct_output(pokraska_arr, arr[6])
        panels_arr = correct_output(panels_arr, arr[7])

    return {
        'Boardervisotazabora': visota_arr,
        'dlinaZabora': dlinaZabora,
        'Boardertolshinastolba': tolshina_arr,
        'Boarderkolvokalitok': kolvo_kalitok,
        'Boarderkolvovorot': kolvo_vorot,
        'Boardershirinavorot': shirinavorot_arr,
        'Boarderpokraska': pokraska_arr,
        'Boarderpanel': panels_arr,
        'result_items': [],
        "result_ysl": [],
        "result_dos": [],
        "result_items_a": [],
        "result": 0,
        'status': 0,
        'kmMkad': kmMkad
    }


def main(request):
    template = 'calculator/boarder.html'
    args = default_values(False, [])
    if request.GET.get('Boarderdlinazabora') is not None:
        visotazabora = float(str(request.GET.get('Boardervisotazabora')).replace(',', '.'))
        dlinazabora = float(str(request.GET.get('Boarderdlinazabora')).replace(',', '.'))
        tolshinastolba = float(str(request.GET.get('Boardertolshinastolba')).replace(',', '.'))
        kolvo_kalitok = float(str(request.GET.get('Boarderkolvokalitok')).replace(',', '.'))
        kolvo_vorot = float(str(request.GET.get('Boarderkolvovorot')).replace(',', '.'))
        shirina_vorot = float(str(request.GET.get('Boardershirinavorot')).replace(',', '.'))
        pokraska = request.GET.get('Boarderpokraska')
        panel = request.GET.get('Boarderpanel')
        args = default_values(True,
                              [visotazabora, dlinazabora, tolshinastolba, kolvo_kalitok, kolvo_vorot, shirina_vorot,
                               pokraska, panel])
        args['status'] = 1
        for i in Boarder3d.objects.all():
            print(i.visota)
            if panel == i.title and float(i.visota) == visotazabora:
                if dlinazabora == 0:
                    continue
                args['result'] += 0.4 * dlinazabora * float(i.price)
                args['result_items'].append({
                    'text': f'Панель 3D с высотой {visotazabora}м {i.title}',
                    'cost': str(round(0.4 * dlinazabora * float(i.price), 2)),
                    'count': int(0.4 * dlinazabora),
                    'ed': 'шт.',
                    'price': f'{round(i.price, 2)}'
                })

        count_stolb = 0
        for i in Boarderdlinastolbov.objects.all():
            if visotazabora == float(i.visota) and float(i.tolshina) == tolshinastolba:
                count_stolb = int((dlinazabora - kolvo_vorot * shirina_vorot - kolvo_kalitok))
                if count_stolb == 0:
                    continue


                args['result'] += count_stolb * float(i.price) / 2.5
                args['result_items'].append({
                    'text': f'Столб с заглушкой 60x60 толщиной {tolshinastolba} мм высотой {visotazabora + 1.2} м + {pokraska.lower()}',
                    'cost': str(round(count_stolb * float(i.price) / 2.5, 2)),
                    'count': f"{int(count_stolb / 2.5)}",
                    'ed': 'шт.',
                    'price': f'{round(i.price, 2)}'

                })

        for i in Boardervorota.objects.all():
            if float(i.shirina) == shirina_vorot and float(i.visota) == visotazabora:
                if kolvo_vorot == 0:
                    continue
                args['result'] += kolvo_vorot * float(i.price)
                args['result_items'].append({
                    'text': f'Ворота {shirina_vorot}x{visotazabora} мм',
                    'cost': str(round(kolvo_vorot * float(i.price), 2)),
                    'count': f"{int(kolvo_vorot)}",
                    'ed': 'шт.',
                    'price': f'{round(i.price, 2)}'
                })

        for i in Boarderkalitka.objects.all():  # Калитки
            if float(i.visota) == visotazabora:
                if kolvo_kalitok == 0:
                    continue
                args['result'] += kolvo_kalitok * float(i.price)
                args['result_items'].append({
                    'text': f'Калитка {1000}x{visotazabora} мм на 1-м столбе',
                    'cost': str(round(kolvo_kalitok * float(i.price), 2)),
                    'count': f"{int(kolvo_kalitok)}",
                    'ed': 'шт.',
                    'price': f'{round(i.price, 2)}'})

        args['result'] += count_stolb * 60 * 3
        args['result_items'].append(
            {'text': f'Крепление скоба + саморез',
             'cost': str(count_stolb * 3 * 60),
             'count': f"{int(count_stolb * 3)}",
             'ed': 'шт.',
             'price': f'{60}'})

        args['result_items'].append({
            'text': "Скидка 2% от стоимости материала", 'cost': str(round(args['result'] * 0.02, 2))
        })
        args['result'] *= 0.98
        args['result_items_a'] = [{
            'text': "Итого за материалы:", 'cost': str(round(args['result'], 2))
        }]
        materiali_price = args['result']
        ystanovkakalitki_price = float(Boarderystanovkavorot.objects.all()[0].price)
        ystanovkavorot_price = float(Boarderystanovkakalitki.objects.all()[0].price)
        args['result'] += ystanovkavorot_price * kolvo_vorot
        if dlinazabora > 0:
            args['result_ysl'].append(
                {
                    'text': "Установочные работы за забор",
                    'cost': 400 * dlinazabora,
                    'count': f"{int(dlinazabora)}",
                    'ed': 'метр забора',
                    'price': 400
                }
            )
            args['result'] += dlinazabora * 400
        if kolvo_vorot != 0:
            args['result_ysl'].append(
                {'text': f'Установка ворот',
                 'cost': str(round(ystanovkavorot_price * kolvo_vorot, 2)),
                 'count': f"{int(kolvo_vorot)}",
                 'ed': 'шт.',
                 'price': round(ystanovkavorot_price, 2)
                 })

        args['result'] += ystanovkakalitki_price * kolvo_kalitok
        if kolvo_kalitok != 0:
            args['result_ysl'].append(
                {
                    'text': f'Установка калитки',
                    'cost': round(ystanovkakalitki_price * kolvo_kalitok, 2),
                    'count': f"{int(kolvo_kalitok)}",
                    'ed': 'шт.',
                    'price': round(ystanovkakalitki_price, 2)
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

    return render(request, template, args)
