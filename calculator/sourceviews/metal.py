from django.shortcuts import render
from calculator.sourcemodels.metal import *


def correct_output(arr, v):
    for i in range(len(arr)):
        if arr[i] == v:
            arr.insert(0, arr[i])
            del arr[i + 1]
            return arr


def default_values(state, arr):
    visota_arr = [float(i[0]) for i in Metalkalitka.objects.all().values_list('visota')]
    tolshina_arr = list(set(float(i[0]) for i in Metaldlinastolbov.objects.all().values_list('tolshina')))
    shirinavorot_arr = list(set(float(i[0]) for i in Metalvorota.objects.all().values_list('shirina')))
    pokraska_arr = list(set(str(i[0]) for i in Metalpokraska.objects.all().values_list('tip')))
    shtaketnik_arr = list(set(str(i[0]) for i in Metalshtaketnik.objects.all().values_list("title")))
    horizontals_arr = list(set(str(i[0]) for i in Metallags.objects.all().values_list("title")))
    polimers_arr = list(set(str(i[0]) for i in Metalshtaketnik.objects.all().values_list("polymer")))
    visota_arr.sort()
    tolshina_arr.sort()
    shirinavorot_arr.sort()
    kolvo_kalitok = [0, 1, 2, 3, 4, 5]
    kolvo_vorot = [0, 1, 2, 3, 4, 5]
    zazor = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    kmMkad = 0
    dlinaZabora = 100
    if state:
        visota_arr = correct_output(visota_arr, arr[0])
        dlinaZabora = str(arr[1])
        tolshina_arr = correct_output(tolshina_arr, arr[2])
        kolvo_kalitok = correct_output(kolvo_kalitok, arr[3])
        kolvo_vorot = correct_output(kolvo_vorot, arr[4])
        shirinavorot_arr = correct_output(shirinavorot_arr, arr[5])
        pokraska_arr = correct_output(pokraska_arr, arr[6])
        shtaketnik_arr = correct_output(shtaketnik_arr, arr[7])
        horizontals_arr = correct_output(horizontals_arr, arr[8])
        polimers_arr = correct_output(polimers_arr, arr[9])
        zazor = correct_output(zazor, arr[10])

    return {
        "Metalzazor": zazor,
        'dlinaZabora': dlinaZabora,
        'Metalvisotazabora': visota_arr,
        'Metaltolshinastolba': tolshina_arr,
        'Metalkolvokalitok': kolvo_kalitok,
        'Metalkolvovorot': kolvo_vorot,
        'Metalshirinavorot': shirinavorot_arr,
        'Metalpokraska': pokraska_arr,
        'Metalshtaketnik': shtaketnik_arr,
        'Metalhorizontals': horizontals_arr,
        'Metalpolimers': polimers_arr,
        'result_items': [],
        "result_ysl": [],
        "result_dos": [],
        "result_items_a": [],
        "result": 0,
        'status': 0,
        'kmMkad': kmMkad
    }


def main(request):
    template = 'calculator/metal.html'
    args = default_values(False, [])
    args['status'] = 0
    if request.GET.get('Metaldlinazabora') is not None:
        visotazabora = float(str(request.GET.get('Metalvisotazabora')).replace(',', '.'))
        dlinazabora = float(str(request.GET.get('Metaldlinazabora')).replace(',', '.'))
        tolshinastolba = float(str(request.GET.get('Metaltolshinastolba')).replace(',', '.'))
        kolvo_kalitok = float(str(request.GET.get('Metalkolvokalitok')).replace(',', '.'))
        kolvo_vorot = float(str(request.GET.get('Metalkolvovorot')).replace(',', '.'))
        shirina_vorot = float(str(request.GET.get('Metalshirinavorot')).replace(',', '.'))
        pokraska = request.GET.get('Metalpokraska')
        shtaketnik = request.GET.get('Metalshtaketnik')
        lagi = request.GET.get('Metalhorizontals')
        import re
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', lagi)]
        s = s[0]


        polimers = request.GET.get('Metalpolimers')
        zazor = int(request.GET.get("Metalzazor"))
        args = default_values(True,
                              [visotazabora, dlinazabora, tolshinastolba, kolvo_kalitok, kolvo_vorot, shirina_vorot,
                               pokraska, shtaketnik, lagi, polimers, zazor])
        args['status'] = 1
        for i in Metallags.objects.all():
            if i.title == lagi:
                if float(i.count_mnsh) * dlinazabora * float(i.price) == 0:
                    continue

                args['result'] += float(i.count_mnsh) * dlinazabora * float(i.price)
                args['result_items'].append({
                    'text': f'Лаги проф.труба 40х20 толщиной 1,5 мм',
                    'cost': str(round(float(i.count_mnsh) * dlinazabora * float(i.price), 2)),
                    'count': str(int(float(i.count_mnsh) * dlinazabora)),
                    'ed': 'п.м.',
                    'price': str(round(i.price, 2))
                })

        for i in Metalshtaketnik.objects.all():
            if i.title == shtaketnik and i.polymer == polimers:
                if visotazabora * dlinazabora * 10 * float(i.price) == 0:
                    continue
                if "Finfold" in shtaketnik:
                    shtaketnik_count = int(dlinazabora / ((0.1 + int(zazor)  / 100)) * visotazabora + 5)
                else:
                    shtaketnik_count = int(dlinazabora / ((0.1 + int(zazor * 2) / 100)) * visotazabora + 5)
                args['result'] += shtaketnik_count * float(i.price)
                args['result_items'].append({
                    'text': f'{i.title}',
                    'cost': str(round(shtaketnik_count * float(i.price), 2)),
                    'count': str(shtaketnik_count),
                    'ed': 'п.м.',
                    'price': str(round(i.price, 2))
                })
        args['result'] += shtaketnik_count * 10 * s
        args['result_items'].append({
            'text': f'Цветные кровельные саморезы',
            'cost': str(shtaketnik_count * 10 * s),
            'count': shtaketnik_count * s,
            'ed': 'шт.',
            'price': str(round(10, 2))
        })

        count = 0
        for i in Metaldlinastolbov.objects.all():
            if visotazabora == float(i.visota) and float(i.tolshina) == tolshinastolba:
                count = int((dlinazabora - kolvo_vorot * shirina_vorot - kolvo_kalitok))
                if count * float(i.price) / 2.5 == 0:
                    continue
                args['result'] += count * float(i.price) / 2.5
                args['result_items'].append({
                    'text': f'Столб 60x30 толщиной {tolshinastolba} мм высотой {visotazabora + 0.8} м',
                    'cost': str(round(count * float(i.price) / 2.5, 2)),
                    'count': str(int(count / 2.5)),
                    'ed': 'шт.',
                    'price': str(round(i.price, 2))

                })

        for i in Metalvorota.objects.all():
            if float(i.shirina) == shirina_vorot and float(i.visota) == visotazabora:
                if kolvo_vorot * float(i.price) == 0:
                    continue
                args['result'] += kolvo_vorot * float(i.price)
                args['result_items'].append({
                    'text': f'Ворота {shirina_vorot}x{visotazabora} мм',
                    'cost': str(round(kolvo_vorot * float(i.price), 2)),
                    'count': str(int(kolvo_vorot)),
                    'ed': 'шт.',
                    'price': str(round(i.price, 2))
                })

        for i in Metalkalitka.objects.all():  # Калитки
            if float(i.visota) == visotazabora:
                if kolvo_kalitok * float(i.price) == 0:
                    continue
                args['result'] += kolvo_kalitok * float(i.price)
                args['result_items'].append({
                    'text': f'Калитка {1000}x{visotazabora} мм на 1-м столбе',
                    'cost': str(round(kolvo_kalitok * float(i.price), 2)),
                    'count': str(int(kolvo_kalitok)),
                    'ed': 'шт.',
                    'price': str(round(i.price, 2))
                })

        for i in Metalpokraska.objects.all():  # Покраска
            if i.tip == pokraska:
                if count * float(i.kolvo) * float(i.price) == 0:
                    continue
                args['result'] += count * float(i.kolvo) * float(i.price)
                args['result_items'].append(
                    {'text': f'{i.tip}',
                     'cost': str(round(count * float(i.kolvo) * float(i.price), 2)),
                     'count': str(int(round(count * float(i.kolvo), 2))),
                     'ed': 'п.м.',
                     'price': str(round(i.price, 2))
                     })

        args['result_items'].append({
            'text': "Скидка 2% от стоимости материала", 'cost': str(round(args['result'] * 0.02, 2))
        })
        args['result'] *= 0.98
        args['result_items_a'] = [{
            'text': "Итого за материалы:", 'cost': str(round(args['result'], 2))
        }]
        materiali_price = args['result']
        ystanovkakalitki_price = float(Metalystanovkavorot.objects.all()[0].price)
        ystanovkavorot_price = float(Metalystanovkakalitki.objects.all()[0].price)
        if ystanovkavorot_price * kolvo_vorot != 0:
            args['result'] += ystanovkavorot_price * kolvo_vorot

            args['result_ysl'].append(
                {'text': f'Установка ворот',
                 'cost': str(round(ystanovkavorot_price * kolvo_vorot, 2)),
                 'count': str(int(round(kolvo_vorot, 2))),
                 'ed': 'шт.',
                 'price': str(round(ystanovkavorot_price, 2))

                 })
        if ystanovkakalitki_price * kolvo_kalitok != 0:
            args['result'] += ystanovkakalitki_price * kolvo_kalitok
            args['result_ysl'].append(
                {
                    'text': f'Установка калитки',
                    'cost': str(round(ystanovkakalitki_price * kolvo_kalitok, 2)),
                    'count': str(int(round(kolvo_kalitok, 2))),
                    'ed': 'шт.',
                    'price': str(round(ystanovkakalitki_price, 2))
                })

        if dlinazabora > 0:
            args['result'] += 400 * dlinazabora
            args['result_ysl'].append(
                {
                    'text': "Установочные работы за забор",
                    'cost': 400 * dlinazabora,
                    'count': f"{int(dlinazabora)}",
                    'ed': 'метр забора',
                    'price': 400
                }
            )

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
