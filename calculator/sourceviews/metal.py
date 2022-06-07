from django.shortcuts import render
from calculator.sourcemodels.metal import *


def default_values():
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
    return {
        'Metalvisotazabora': visota_arr,
        'Metaltolshinastolba': tolshina_arr,
        'Metalkolvokalitok': [0, 1, 2, 3, 4, 5],
        'Metalkolvovorot': [0, 1, 2, 3, 4, 5],
        'Metalshirinavorot': shirinavorot_arr,
        'Metalpokraska': pokraska_arr,
        'Metalshtaketnik': shtaketnik_arr,
        'Metalhorizontals': horizontals_arr,
        'Metalpolimers': polimers_arr
    }


def main(request):
    template = 'calculator/metal.html'
    args = default_values()
    args['result_items'] = []
    args['result_ysl'] = []
    args['result_dos'] = []
    args['result_items_a'] = []
    args['result'] = 0
    args['status'] = 0
    if request.GET.get('Metaldlinazabora') is not None:
        args['status'] = 1
        visotazabora = float(str(request.GET.get('Metalvisotazabora')).replace(',', '.'))
        dlinazabora = float(str(request.GET.get('Metaldlinazabora')).replace(',', '.'))
        tolshinastolba = float(str(request.GET.get('Metaltolshinastolba')).replace(',', '.'))
        kolvo_kalitok = float(str(request.GET.get('Metalkolvokalitok')).replace(',', '.'))
        kolvo_vorot = float(str(request.GET.get('Metalkolvovorot')).replace(',', '.'))
        shirina_vorot = float(str(request.GET.get('Metalshirinavorot')).replace(',', '.'))
        pokraska = request.GET.get('Metalpokraska')
        shtaketnik = request.GET.get('Metalshtaketnik')
        lagi = request.GET.get('Metalhorizontals')
        polimers = request.GET.get('Metalpolimers')

        for i in Metallags.objects.all():
            if i.title == lagi:
                if float(i.count_mnsh) * dlinazabora * float(i.price) == 0:
                    continue
                args['result'] += float(i.count_mnsh) * dlinazabora * float(i.price)
                args['result_items'].append({
                    'text': f'Лаги проф.труба 40х20 толщиной 1,5 мм',
                    'cost': str(round(float(i.count_mnsh) * dlinazabora * float(i.price), 2)) + " руб.",
                    'count': str(int(float(i.count_mnsh) * dlinazabora)) + " шт.",
                    'ed': 'п.м.',
                    'price': str(round(i.price, 2)) + " руб."
                })

        for i in Metalshtaketnik.objects.all():
            if i.title == shtaketnik and i.polymer == polimers:
                if visotazabora * dlinazabora * 10 * float(i.price) == 0:
                    continue
                args['result'] += visotazabora * dlinazabora * 10 * float(i.price)
                args['result_items'].append({
                    'text': f'{i.title}',
                    'cost': str(round(visotazabora * dlinazabora * 10 * float(i.price), 2)) + " руб.",
                    'count': str(int(visotazabora * dlinazabora * 10)) + " шт.",
                    'ed': 'п.м.',
                    'price': str(round(i.price, 2)) + " руб."
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
                    'cost': str(round(count * float(i.price) / 2.5, 2)) + ' руб.',
                    'count': str(int(count / 2.5)) + " шт.",
                    'ed': 'шт.',
                    'price': str(round(i.price, 2)) + " руб."

                })

        for i in Metalvorota.objects.all():
            if float(i.shirina) == shirina_vorot and float(i.visota) == visotazabora:
                if kolvo_vorot * float(i.price) == 0:
                    continue
                args['result'] += kolvo_vorot * float(i.price)
                args['result_items'].append({
                    'text': f'Ворота {shirina_vorot}x{visotazabora} мм',
                    'cost': str(round(kolvo_vorot * float(i.price), 2)) + ' руб.',
                    'count': str(int(kolvo_vorot)) + " шт.",
                    'ed': 'шт.',
                    'price': str(round(i.price, 2)) + " руб."
                    })

        for i in Metalkalitka.objects.all():  # Калитки
            if float(i.visota) == visotazabora:
                if kolvo_kalitok * float(i.price) == 0:
                    continue
                args['result'] += kolvo_kalitok * float(i.price)
                args['result_items'].append({
                    'text': f'Калитка {1000}x{visotazabora} мм на 1-м столбе',
                    'cost': str(round(kolvo_kalitok * float(i.price), 2)) + " руб.",
                    'count': str(int(kolvo_kalitok)) + " шт.",
                    'ed': 'шт.',
                    'price': str(round(i.price, 2)) + " руб."
                })

        for i in Metalpokraska.objects.all():  # Покраска
            if i.tip == pokraska:
                if count * float(i.kolvo) * float(i.price) == 0:
                    continue
                args['result'] += count * float(i.kolvo) * float(i.price)
                args['result_items'].append(
                    {'text': f'{i.tip}',
                     'cost': str(round(count * float(i.kolvo) * float(i.price), 2)) + " руб.",
                     'count': str(int(round(count * float(i.kolvo), 2))) + " шт.",
                     'ed': 'п.м.',
                     'price': str(round(i.price, 2)) + " руб."
                     })

        args['result_items'].append({
            'text': "Скидка 2% от стоимости материала", 'cost': str(round(args['result'] * 0.02, 2)) + " руб."
        })
        args['result'] *= 0.98
        args['result_items_a'] = [{
            'text': "Итого за материалы:", 'cost': str(round(args['result'], 2)) + " руб."
        }]
        materiali_price = args['result']
        ystanovkakalitki_price = float(Metalystanovkavorot.objects.all()[0].price)
        ystanovkavorot_price = float(Metalystanovkakalitki.objects.all()[0].price)
        if ystanovkavorot_price * kolvo_vorot != 0:
            args['result'] += ystanovkavorot_price * kolvo_vorot

            args['result_ysl'].append(
                {'text': f'Установка ворот',
                 'cost': str(round(ystanovkavorot_price * kolvo_vorot, 2)) + " руб.",
                     'count': str(int(round(kolvo_vorot, 2))) + " шт.",
                     'ed': 'шт.',
                     'price': str(round(ystanovkavorot_price, 2)) + " руб."

                 })
        if ystanovkakalitki_price * kolvo_kalitok != 0:
            args['result'] += ystanovkakalitki_price * kolvo_kalitok
            args['result_ysl'].append(
                {
                    'text': f'Установка калитки',
                    'cost': str(round(ystanovkakalitki_price * kolvo_kalitok, 2)) + " руб.",
                     'count': str(int(round(kolvo_kalitok, 2))) + " шт.",
                     'ed': 'шт.',
                     'price': str(round(ystanovkakalitki_price, 2)) + " руб."

                })

        args['result_ysl_a'] = [{
            'text': "Итого за услуги:", 'cost': str(round(args['result'] - materiali_price, 2)) + " руб."
        }]

        kmmkad = int(float(request.GET.get('kmMkad')))
        dostavka = kmmkad * 30
        if kmmkad > 30:
            kmmkad_res = kmmkad - 30
            dostavka += kmmkad_res * 65
        args['result'] += dostavka
        args['result_dos'].append(
            {'text': f'Доставка до участка',
             'cost': str(round(dostavka, 2)) + " руб.",
                     'count': str(int(round(kmmkad, 2))) + " км"
             })

    args['result'] = str(round(args['result'], 2)) + ' руб.'
    return render(request, template, args)
