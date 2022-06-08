from django.shortcuts import render
from calculator.sourcemodels.navesi import *


def default_values():
    visota = list(set(float(i[0]) for i in Navesidlinastolbov.objects.all().values_list('visota')))
    tolshina = list(set(str(i[0]) for i in Navesidlinastolbov.objects.all().values_list('tolshina')))
    typ = list(set(str(i[0]) for i in Navesifermi.objects.all().values_list('name')))
    krovla = list(set(str(i[0]) for i in Navesikrov.objects.all().values_list('name')))
    fermi = list(set(str(i[0]) for i in Navesibokferma.objects.all().values_list('name')))
    visota.sort()
    return {
        'NavesivisotaZabora': visota,
        'Navesityp': typ,
        'Navesirazmer': tolshina,
        'Navesimethod': ['Забивание и трамбовка щебнем', 'На анкерах', 'Бетонирование столбов',
                         'На винтовых сваях диам. 76 мм'],
        'Navesikrovlya': krovla,
        'Navesifermi': fermi
    }


def main(request):
    args = default_values()
    args['result_items'] = []
    args['result_ysl'] = []
    args['result_dos'] = []
    args['result_items_a'] = []
    args['result'] = 0
    args['status'] = 0
    print(request.GET)
    if request.GET.get('NavesidlinaZabora') is not None:
        args['status'] = 1
        typ = request.GET.get('Navesityp')
        dlinazabora = float(request.GET.get('NavesidlinaZabora').replace(',', '.'))
        shirina = float(request.GET.get('NavesishirinaZabora').replace(',', '.'))
        tolshinastolba = request.GET.get('Navesirazmer')
        razmer = request.GET.get('Navesirazmer')
        method = request.GET.get('Navesimethod')
        krovlya = request.GET.get('Navesikrovlya')
        visota = float(request.GET.get('NavesivisotaZabora').replace(',', '.'))
        dopfermi = request.GET.get('Navesifermi')
        for i in Navesidlinastolbov.objects.all():
            if float(i.visota) == float(visota) and i.tolshina == tolshinastolba:
                count = dlinazabora  # TODO: хз как это формируется
                cost = count * float(i.price)
                if cost == 0:
                    continue
                args['result'] += cost
                args['result_items'].append({
                    'text': f'Столбы профильные 100x100 мм, толщина 3 мм L={visota} м',
                    'cost': f"{round(cost, 2)} руб.",
                    'count': f"{int(count)} шт.",
                    'ed': 'шт.',
                    'price': f"{round(float(i.price), 2)} руб."
                })

        for i in Navesibalka.objects.all():
            if i.tolshina == tolshinastolba:
                count = dlinazabora * 2
                cost = count * float(i.price)
                if cost == 0:
                    continue
                args['result'] += cost
                args['result_items'].append({
                    'text': f'Опорная балка под фермы 100x1 мм, толщина 2 мм',
                    'cost': f"{round(cost, 2)} руб.",
                    'count': f"{int(count)} шт.",
                    'ed': 'п.м.',
                    'price': f"{round(float(i.price), 2)} руб."
                })

        for i in Navesifermi.objects.all():
            if i.name == typ:
                count = int(dlinazabora / 2) + 1
                cost = count * float(i.price)
                if cost == 0:
                    continue
                args['result'] += cost
                args['result_items'].append({
                    'text': f'Ферма {i.name.lower()}',
                    'cost': f"{round(cost, 2)} руб.",
                    'count': f"{int(count)} шт.",
                    'ed': 'шт.',
                    'price': f"{round(float(i.price), 2)} руб."
                })

        for i in Navesiobrfermi.objects.all():
            count = dlinazabora * shirina * 2 + dlinazabora
            cost = count * float(i.price)
            if cost == 0:
                continue
            args['result'] += cost
            args['result_items'].append({
                'text': f'{i.name}',
                'cost': f"{round(cost, 2)} руб.",
                'count': f"{int(count)} шт.",
                'ed': 'п.м.',
                'price': f"{round(float(i.price), 2)} руб."
            })

        for i in Navesikrov.objects.all():
            if i.name == krovlya:
                count = dlinazabora * shirina
                cost = count * float(i.price)
                if cost == 0:
                    continue
                args['result'] += cost
                args['result_items'].append({
                    'text': f'{i.name}',
                    'cost': f"{round(cost, 2)} руб.",
                    'count': f"{int(count)} шт.",
                    'ed': 'м2',
                    'price': f"{round(float(i.price), 2)} руб."
                })

        for i in Navesibokferma.objects.all():
            if i.name == dopfermi:
                count = dlinazabora * 2
                cost = count * float(i.price)
                if cost == 0:
                    continue
                args['result'] += cost
                args['result_items'].append({
                    'text': f'Боковая ферма',
                    'cost': f"{round(cost, 2)} руб.",
                    'count': f"{int(count)} шт.",
                    'ed': 'п.м.',
                    'price': f"{round(float(i.price), 2)} руб."
                })
        for i in Navesikraska.objects.all():
            count = dlinazabora * shirina
            cost = count * float(i.price)
            if cost == 0:
                continue
            args['result'] += cost
            args['result_items'].append({
                'text': f'{i.name}',
                'cost': f"{round(cost, 2)} руб.",
                'count': f"{int(count)} шт.",
                'ed': 'м2',
                'price': f"{round(float(i.price), 2)} руб."
            })

        args['result_items'].append({
            'text': "Скидка 2% от стоимости материала", 'cost': str(round(args['result'] * 0.02, 2)) + " руб."
        })
        args['result'] *= 0.98
        args['result_items_a'] = [{
            'text': "Итого за материалы:", 'cost': str(round(args['result'], 2)) + " руб."
        }]
        materiali_price = args['result']

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
    template = 'calculator/navesi.html'
    return render(request, template, args)


"""
1. Столбы: цена - размер и толщина и высота + 
2. Балка под фермы: цена - размер и толщина +
3. Ферма: зависит от выбора фермы +
4. Обрешетка фермы: всегда одна  !! +
5. Кровельный материал: зависит от выбора кров материала +
6. Конек металлический - всегда один и тот же  !! +
7. Боковая ферма - если выбирают то одно и то же +
8. Ветровая планка - всегда одна и та же  !! 
9. Покраска - всегда одинакова !! 
41500 mnosh = 
47 900 mnsoh = 
54 300 mnosh = 
54 300 mnosh = 
"""
