from django.shortcuts import render
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
    args['result_items_a'] = []
    args['result'] = 0
    args['status'] = 0
    if request.GET.get('Rabizadlinazabora') is not None:
        args['status'] = 1
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

                if count == 0:
                    continue

                args['result'] += count * float(i.price) / 2.5
                args['result_items'].append({'text': f'Столб 60x30 толщиной {tolshinastolba} мм высотой {visotazabora + 0.8} м',
                                             'cost': str(round(count * float(i.price) / 2.5, 2)) + " руб.",
                                             'count': str(int(count / 2.5)) + " шт.",
                                             'ed': 'шт.',
                                             'price': str(round(i.price, 2)) + " руб."
                                             })

        for i in Rabizasetka.objects.all():  # СЕТКА
            if visotazabora == float(i.visota) and float(i.tolshina) == tolshinasetki:
                if dlinazabora / 10 == 0:
                    continue
                args['result'] += dlinazabora / 10 * float(i.price)
                args['result_items'].append(
                    {'text': f'Сетка с высотой {visotazabora} м и толщиной {tolshinasetki} мм',
                     'cost': str(round(dlinazabora / 10 * float(i.price), 2)) + " руб.",
                     'count': str(int(dlinazabora / 10)) + " шт.",
                     'ed': 'рул.',
                     'price': str(round(i.price, 2)) + " руб."
                     })

        for i in Rabizavorota.objects.all():  # ВОРОТА
            if float(i.shirina) == shirina_vorot and float(i.visota) == visotazabora:
                if kolvo_vorot == 0:
                    continue
                args['result'] += kolvo_vorot * float(i.price)
                args['result_items'].append({'text': f'Ворота {shirina_vorot}x{visotazabora} мм',
                                             'cost': str(round(kolvo_vorot * float(i.price), 2)) + " руб.",
                                             'count': str(int(kolvo_vorot)) + " шт.",
                                             'ed': 'шт.',
                                             'price': str(round(i.price, 2)) + " руб."
                                             })

        for i in Rabizakalitka.objects.all():  # Калитки
            if float(i.visota) == visotazabora:
                if kolvo_kalitok == 0:
                    continue
                args['result'] += kolvo_kalitok * float(i.price)
                args['result_items'].append({'text': f'Калитка {1000}x{visotazabora} мм на 1-м столбе',
                                             'cost': str(round(kolvo_kalitok * float(i.price), 2)) + " руб.",
                                             'count': str(int(kolvo_kalitok)) + " шт.",
                                             'ed': 'шт.',
                                             'price': str(round(i.price, 2)) + " руб."
                                             })

        for i in Rabizapokraska.objects.all():  # Покраска
            if i.tip == pokraska:
                if count * float(i.kolvo) == 0:
                    continue
                args['result'] += count * float(i.kolvo) * float(i.price)
                args['result_items'].append(
                    {'text': f'{i.tip}',
                     'cost': str(round(count * float(i.kolvo) * float(i.price), 2)) + " руб.",
                     'count': str(int(count * float(i.kolvo))) + " шт.",
                     'ed': 'шт.',
                     'price': str(round(i.price, 2)) + " руб."
                     })

                # АРМАТУРА
        if armatura == "Один ряд":
            mnosh = 1
        elif armatura == "Два ряда":
            mnosh = 2
        else:
            mnosh = 0
        armatura_price = float(Rabizaarmatura.objects.all()[0].price)
        args['result'] += dlinazabora * mnosh * armatura_price
        if dlinazabora * mnosh != 0:
            args['result_items'].append(
                {'text': f'Арматура толщиной 10 мм',
                 'cost': str(round(dlinazabora * mnosh * float(armatura_price), 2)) + ' руб.',
                 'count': str(int(mnosh * dlinazabora)) + " шт.",
                 'ed': 'п.м.',
                 'price': str(round(armatura_price, 2)) + " руб."
                 })
            args['result_items'].append({
                'text': "Скидка 2% от стоимости материала", 'cost': str(round(args['result'] * 0.02, 2)) + " руб."
            })
        args['result'] *= 0.98
        args['result_items_a'] = [{
            'text': "Итого за материалы:", 'cost': str(round(args['result'], 2)) + " руб."
        }]
        materiali_price = args['result']
        ystanovkakalitki_price = float(Rabizaystanovkakalitki.objects.all()[0].price)
        ystanovkavorot_price = float(Rabizaystanovkavorot.objects.all()[0].price)
        args['result'] += ystanovkavorot_price * kolvo_vorot
        if kolvo_vorot != 0:
            args['result_ysl'].append(
                {'text': f'Установка ворот',
                 'cost': str(round(ystanovkavorot_price * kolvo_vorot, 2)) + " руб.",
                 'count': str(int(kolvo_vorot)) + " шт.",
                 'ed': 'шт.',
                 'price': str(round(ystanovkavorot_price, 2)) + " руб."
                 })

        args['result'] += ystanovkakalitki_price * kolvo_kalitok
        if kolvo_kalitok != 0:
            args['result_ysl'].append(
                {'text': f'Установка калитки ({kolvo_kalitok} шт.) - {ystanovkakalitki_price * kolvo_kalitok} рублей за калитку',
                 'cost': str(round(ystanovkakalitki_price * kolvo_kalitok, 2)) + " руб.",
                 'count': str(int(kolvo_kalitok)) + " шт.",
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
    args['result'] = str(round(args['result'], 2)) + " руб."
    return render(request, template, args)  # used at first page load
