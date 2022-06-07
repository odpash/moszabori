from django.shortcuts import render
from calculator.sourcemodels.boarder import *


def default_values():
    visota_arr = [float(i[0]) for i in Boarderkalitka.objects.all().values_list('visota')]
    tolshina_arr = list(set(float(i[0]) for i in Boarderdlinastolbov.objects.all().values_list('tolshina')))
    shirinavorot_arr = list(set(float(i[0]) for i in Boardervorota.objects.all().values_list('shirina')))
    pokraska_arr = list(set(str(i[0]) for i in Boarderpokraska.objects.all().values_list('tip')))
    panels_arr = list(set(str(i[0]) for i in Boarder3d.objects.all().values_list('title')))
    visota_arr.sort()
    tolshina_arr.sort()
    shirinavorot_arr.sort()
    return {
        'Boardervisotazabora': visota_arr,
        'Boardertolshinastolba': tolshina_arr,
        'Boarderkolvokalitok': [0, 1, 2, 3, 4, 5],
        'Boarderkolvovorot': [0, 1, 2, 3, 4, 5],
        'Boardershirinavorot': shirinavorot_arr,
        'Boarderpokraska': pokraska_arr,
        'Boarderpanel': panels_arr
    }


def main(request):
    template = 'calculator/boarder.html'
    args = default_values()
    args['result_items'] = []
    args['result_ysl'] = []
    args['result_dos'] = []
    args['result_items_a'] = []
    args['result'] = 0
    args['status'] = 0
    if request.GET.get('Boarderdlinazabora') is not None:
        args['status'] = 1
        visotazabora = float(str(request.GET.get('Boardervisotazabora')).replace(',', '.'))
        dlinazabora = float(str(request.GET.get('Boarderdlinazabora')).replace(',', '.'))
        tolshinastolba = float(str(request.GET.get('Boardertolshinastolba')).replace(',', '.'))
        kolvo_kalitok = float(str(request.GET.get('Boarderkolvokalitok')).replace(',', '.'))
        kolvo_vorot = float(str(request.GET.get('Boarderkolvovorot')).replace(',', '.'))
        shirina_vorot = float(str(request.GET.get('Boardershirinavorot')).replace(',', '.'))
        pokraska = request.GET.get('Boarderpokraska')
        panel = request.GET.get('Boarderpanel')
        for i in Boarder3d.objects.all():
            if panel == i.title and float(i.visota) == visotazabora:
                if dlinazabora == 0:
                    continue
                args['result'] += 0.4 * dlinazabora * float(i.price)
                args['result_items'].append({
                    'text': f'Панель 3D с высотой {visotazabora}м {i.title}',
                    'cost': str(round(0.4 * dlinazabora * float(i.price), 2)) + " руб.",
                    'count': f"{0.4 * dlinazabora} шт.",
                    'ed': 'шт.',
                    'price': f'{round(i.price, 2)} руб.'
                })

        count = 0
        for i in Boarderdlinastolbov.objects.all():
            if visotazabora == float(i.visota) and float(i.tolshina) == tolshinastolba:
                count = int((dlinazabora - kolvo_vorot * shirina_vorot - kolvo_kalitok))
                if count == 0:
                    continue
                args['result'] += count * float(i.price) / 2.5
                args['result_items'].append({
                    'text': f'Столб 60x30 толщиной {tolshinastolba} мм высотой {visotazabora + 0.8} м',
                    'cost': str(round(count * float(i.price) / 2.5, 2)) + " руб.",
                    'count': f"{int(count / 2.5)} шт.",
                    'ed': 'шт.',
                    'price': f'{round(i.price, 2)} руб.'

                })

        for i in Boardervorota.objects.all():
            if float(i.shirina) == shirina_vorot and float(i.visota) == visotazabora:
                if kolvo_vorot == 0:
                    continue
                args['result'] += kolvo_vorot * float(i.price)
                args['result_items'].append({
                    'text': f'Ворота {shirina_vorot}x{visotazabora} мм',
                    'cost': str(round(kolvo_vorot * float(i.price), 2)) + " руб.",
                    'count': f"{int(kolvo_vorot)} шт.",
                    'ed': 'шт.',
                    'price': f'{round(i.price, 2)} руб.'
                })

        for i in Boarderkalitka.objects.all():  # Калитки
            if float(i.visota) == visotazabora:
                if kolvo_kalitok == 0:
                    continue
                args['result'] += kolvo_kalitok * float(i.price)
                args['result_items'].append({
                    'text': f'Калитка {1000}x{visotazabora} мм на 1-м столбе',
                    'cost': str(round(kolvo_kalitok * float(i.price), 2)) + " руб.",
                    'count': f"{int(kolvo_kalitok)} шт.",
                    'ed': 'шт.',
                    'price': f'{round(i.price, 2)} руб.'})

        for i in Boarderpokraska.objects.all():  # Покраска
            if i.tip == pokraska:
                if count * float(i.kolvo) == 0:
                    continue
                args['result'] += count * float(i.kolvo) * float(i.price)
                args['result_items'].append(
                    {'text': f'{i.tip}',
                     'cost': str(round(count * float(i.kolvo) * float(i.price), 2)) + " руб.",
                     'count': f"{int(count * float(i.kolvo))} шт.",
                     'ed': 'шт.',
                     'price': f'{round(i.price, 2)} руб.'})

        args['result_items'].append({
            'text': "Скидка 2% от стоимости материала", 'cost': str(round(args['result'] * 0.02, 2)) + " руб."
        })
        args['result'] *= 0.98
        args['result_items_a'] = [{
            'text': "Итого за материалы:", 'cost': str(round(args['result'], 2)) + " руб."
        }]
        materiali_price = args['result']
        ystanovkakalitki_price = float(Boarderystanovkavorot.objects.all()[0].price)
        ystanovkavorot_price = float(Boarderystanovkakalitki.objects.all()[0].price)
        args['result'] += ystanovkavorot_price * kolvo_vorot
        if kolvo_vorot != 0:
            args['result_ysl'].append(
                {'text': f'Установка ворот',
                 'cost': str(round(ystanovkavorot_price * kolvo_vorot, 2)) + " руб.",
                 'count': f"{int(kolvo_vorot)} шт.",
                 'ed': 'шт.',
                 'price': f'{round(ystanovkavorot_price, 2)} руб.'
                 })

        args['result'] += ystanovkakalitki_price * kolvo_kalitok
        if kolvo_kalitok != 0:
            args['result_ysl'].append(
                {
                    'text': f'Установка калитки',
                    'cost': round(ystanovkakalitki_price * kolvo_kalitok, 2),
                    'count': f"{int(kolvo_kalitok)} шт.",
                    'ed': 'шт.',
                    'price': f'{round(ystanovkakalitki_price, 2)} руб.'
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

    args['result'] = str(round(args['result'], 2)) + " руб."
    return render(request, template, args)
