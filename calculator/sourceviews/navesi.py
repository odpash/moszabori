from django.shortcuts import render
from calculator.sourcemodels.navesi import *



def correct_output(arr, v):
    for i in range(len(arr)):
        if arr[i] == v:
            arr.insert(0, arr[i])
            del arr[i + 1]
            return arr


def default_values(state, arr):
    visota = list(set(float(i[0]) for i in Navesidlinastolbov.objects.all().values_list('visota')))
    tolshina = list(set(str(i[0]) for i in Navesidlinastolbov.objects.all().values_list('tolshina')))
    typ = list(set(str(i[0]) for i in Navesifermi.objects.all().values_list('name')))
    krovla = list(set(str(i[0]) for i in Navesikrov.objects.all().values_list('name')))
    fermi = list(set(str(i[0]) for i in Navesibokferma.objects.all().values_list('name')))
    visota.sort()  # dlinazabora, shirina, tolshinastolba, method, krovlya, visota, dopfermi
    kolvo_kalitok = [0, 1, 2, 3, 4, 5]
    kolvo_vorot = [0, 1, 2, 3, 4, 5]
    kmMkad = 0
    dlinaZabora = 100
    method = ['Забивание и трамбовка щебнем', 'На анкерах', 'Бетонирование столбов',
                         'На винтовых сваях диам. 76 мм']
    shirinaZabora = 0
    if state:
        dlinaZabora = str(arr[0])
        shirinaZabora = str(arr[1])
        tolshina = correct_output(tolshina, arr[2])
        method = correct_output(method, arr[3])
        krovla = correct_output(krovla, arr[4])
        visota = correct_output(visota, arr[5])
        fermi = correct_output(fermi, arr[6])


    return {
        'dlinaZabora': dlinaZabora,
        'shirinaZabora': shirinaZabora,
        'NavesivisotaZabora': visota,
        'Navesityp': typ,
        'Navesirazmer': tolshina,
        'Navesimethod': method,
        'Navesikrovlya': krovla,
        'Navesifermi': fermi,
        'result_items': [],
        "result_ysl": [],
        "result_dos": [],
        "result_items_a": [],
        "result": 0,
        'status': 0,
        'kmMkad': kmMkad
    }


def main(request):
    args = default_values(False, [])
    if request.GET.get('NavesidlinaZabora') is not None:
        typ = request.GET.get('Navesityp')
        dlinazabora = float(request.GET.get('NavesidlinaZabora').replace(',', '.'))
        shirina = float(request.GET.get('NavesishirinaZabora').replace(',', '.'))
        tolshinastolba = request.GET.get('Navesirazmer')
        method = request.GET.get('Navesimethod')
        krovlya = request.GET.get('Navesikrovlya')
        visota = float(request.GET.get('NavesivisotaZabora').replace(',', '.'))
        dopfermi = request.GET.get('Navesifermi')
        args = default_values(True,
                              [dlinazabora, shirina, tolshinastolba, method, krovlya, visota, dopfermi])
        args['status'] = 1
        for i in Navesidlinastolbov.objects.all():
            if float(i.visota) == float(visota) and i.tolshina == tolshinastolba:
                count = dlinazabora * 2 # TODO: хз как это формируется
                cost = count * float(i.price)
                if cost == 0:
                    continue
                args['result'] += cost
                args['result_items'].append({
                    'text': f'Столбы профильные 100x100 мм, толщина 3 мм L={visota} м',
                    'cost': f"{round(cost, 2)}",
                    'count': f"{int(count)}",
                    'ed': 'шт.',
                    'price': f"{round(float(i.price), 2)}"
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
                    'cost': f"{round(cost, 2)}",
                    'count': f"{int(count)}",
                    'ed': 'п.м.',
                    'price': f"{round(float(i.price), 2)}"
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
                    'cost': f"{round(cost, 2)}",
                    'count': f"{int(count)}",
                    'ed': 'шт.',
                    'price': f"{round(float(i.price), 2)}"
                })

        for i in Navesiobrfermi.objects.all():
            count = dlinazabora * shirina * 2 + dlinazabora
            cost = count * float(i.price)
            if cost == 0:
                continue
            args['result'] += cost
            args['result_items'].append({
                'text': f'{i.name}',
                'cost': f"{round(cost, 2)}",
                'count': f"{int(count)}",
                'ed': 'п.м.',
                'price': f"{round(float(i.price), 2)}"
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
                    'cost': f"{round(cost, 2)}",
                    'count': f"{int(count)}",
                    'ed': 'м2',
                    'price': f"{round(float(i.price), 2)}"
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
                    'cost': f"{round(cost, 2)}",
                    'count': f"{int(count)}",
                    'ed': 'п.м.',
                    'price': f"{round(float(i.price), 2)}"
                })
        for i in Navesikraska.objects.all():
            count = dlinazabora * shirina
            cost = count * float(i.price)
            if cost == 0:
                continue
            args['result'] += cost
            args['result_items'].append({
                'text': f'{i.name}',
                'cost': f"{round(cost, 2)}",
                'count': f"{int(count)}",
                'ed': 'м2',
                'price': f"{round(float(i.price), 2)}"
            })

        args['result_items'].append({
            'text': "Скидка 2% от стоимости материала", 'cost': str(round(args['result'] * 0.02, 2))
        })
        args['result'] *= 0.98
        args['result_items_a'] = [{
            'text': "Итого за материалы:", 'cost': str(round(args['result'], 2))
        }]
        materiali_price = args['result']

        for i in Navesiystanovka.objects.all():
            if method == i.name:
                count = 1
                cost = count * dlinazabora * shirina * visota * float(i.price)
                if cost != 0:
                    args['result'] += cost
                    args['result_ysl'].append({
                        'text': f'Установка навеса ({i.name})',
                        'count': 1,
                        'ed': 'шт.',
                        'price': f"{round(cost, 2)}",
                        'cost': f"{round(cost , 2)}"
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
41500 mnosh = 1
47 900 mnsoh = 
54 300 mnosh = 
54 300 mnosh = 
"""
