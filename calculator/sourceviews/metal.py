from django.shortcuts import render
from calculator.sourcemodels.metal import *



def default_values():
    visota_arr = [float(i[0]) for i in Metalkalitka.objects.all().values_list('visota')]
    tolshina_arr = list(set(float(i[0]) for i in Metaldlinastolbov.objects.all().values_list('tolshina')))
    shirinavorot_arr = list(set(float(i[0]) for i in Metalvorota.objects.all().values_list('shirina')))
    pokraska_arr = list(set(str(i[0]) for i in Metalpokraska.objects.all().values_list('tip')))
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
        'Metalshtaketnik': '',
        'Metalhorizontals': '',
        'Metalpolimers': ''
    }


def main(request):
    template = 'calculator/metal.html'
    args = default_values()
    args['result_items'] = []
    args['result_ysl'] = []
    args['result_dos'] = []
    args['result_items_a'] = []
    args['result'] = 0
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
        polimers = request.GET.get('Metalpolimers')

        count = 0
        for i in Metaldlinastolbov.objects.all():  # ЦЕНА СТОЛБОВ
            if visotazabora == float(i.visota) and float(i.tolshina) == tolshinastolba:
                count = int((dlinazabora - kolvo_vorot * shirina_vorot - kolvo_kalitok))
                print(count)
                args['result'] += count * float(i.price) / 2.5
                args['result_items'].append({
                                                'text': f'Столб 60x30 толщиной {tolshinastolba} мм высотой {visotazabora + 0.8} м ({count / 2.5} шт.) - {i.price} рублей за столб',
                                                'cost': round(count * float(i.price) / 2.5, 2)})

        for i in Metalvorota.objects.all():  # ВОРОТА
            if float(i.shirina) == shirina_vorot and float(i.visota) == visotazabora:
                args['result'] += kolvo_vorot * float(i.price)
                args['result_items'].append({
                                                'text': f'Ворота {shirina_vorot}x{visotazabora} мм ({kolvo_vorot} шт.) - {i.price} рублей за штуку',
                                                'cost': round(kolvo_vorot * float(i.price), 2)})

        for i in Metalkalitka.objects.all():  # Калитки
            if float(i.visota) == visotazabora:
                args['result'] += kolvo_kalitok * float(i.price)
                args['result_items'].append({
                                                'text': f'Калитка {1000}x{visotazabora} мм на 1-м столбе ({kolvo_kalitok} шт.) - {i.price} рублей за штуку',
                                                'cost': round(kolvo_kalitok * float(i.price), 2)})

        for i in Metalpokraska.objects.all():  # Покраска
            if i.tip == pokraska:
                args['result'] += count * float(i.kolvo) * float(i.price)
                args['result_items'].append(
                    {'text': f'{i.tip} ({round(count * float(i.kolvo), 2)} шт.) - {i.price} рублей за штуку',
                     'cost': round(count * float(i.kolvo) * float(i.price), 2)})

        args['result_items'].append({
            'text': "Скидка 2% от стоимости материала", 'cost': round(args['result'] * 0.02, 2)
        })
        args['result'] *= 0.98
        args['result_items_a'] = [{
            'text': "Итого за материалы:", 'cost': round(args['result'], 2)
        }]
        materiali_price = args['result']
        ystanovkakalitki_price = float(Metalystanovkavorot.objects.all()[0].price)
        ystanovkavorot_price = float(Metalystanovkakalitki.objects.all()[0].price)
        args['result'] += ystanovkavorot_price * kolvo_vorot

        args['result_ysl'].append(
            {'text': f'Установка ворот ({kolvo_vorot} шт.) - {ystanovkavorot_price * kolvo_vorot} рублей за ворота',
             'cost': round(ystanovkavorot_price * kolvo_vorot, 2)})

        args['result'] += ystanovkakalitki_price * kolvo_kalitok
        args['result_ysl'].append(
            {
                'text': f'Установка калитки ({kolvo_kalitok} шт.) - {ystanovkakalitki_price * kolvo_kalitok} рублей за калитку',
                'cost': round(ystanovkakalitki_price * kolvo_kalitok, 2)})

        args['result_ysl_a'] = [{
            'text': "Итого за услуги:", 'cost': round(args['result'] - materiali_price, 2)
        }]

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
    return render(request, template, args)
