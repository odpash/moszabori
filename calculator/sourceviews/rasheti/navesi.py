def main(args, data):
    print(data)
    args['result'] = 0.0  # result value
    args['result_items'] = []
    data['shirinaZabora'] = int(float(data['shirinaZabora']))
    data['dlinaZabora'] = int(float(data['dlinaZabora']))
    stolbi = data['dlinaZabora']
    stolbi_mnsoh = [i['price'] for i in args['Navesirazmer'] if i['value'] == data['razmer']][0]
    stolbi_mnsoh2 = [i['mnosh'] for i in args['NavesivisotaZabora'] if i['value'] == data['visotaZabora']][0]
    if stolbi % 2 != 0:
        stolbi += 1
    visota = float(data['visotaZabora'])
    navesiPrice = [i['price'] for i in args['Navesirazmer'] if i['value'] == data['razmer']][0]
    args['result_items'].append({'text': "Столбы профильные", 'cost': int(stolbi * stolbi_mnsoh * stolbi_mnsoh2)})
    args['result_items'].append({'text': data['razmer'], 'cost': int(data['dlinaZabora'] * 2 * navesiPrice)})

    fermiPrice = [i['price'] for i in args['Navesifermi'] if i['value'] == data['fermi']][0]
    args['result_items'].append({'text': 'Боковая ферма', 'cost': data['dlinaZabora'] * int(data['fermi']) * int(fermiPrice)})
    args['result_items'].append({'text': "Покраска цветной эмалью 3 в 1 Dali столбов, обрешетки и фермы", 'cost': 400 * data['dlinaZabora'] * data['shirinaZabora']})


    methodPrice = [i['price'] for i in args['Navesimethod'] if i['value'] == data['method']][0]
    args['result_items'].append({'text': data['method'], 'cost': int(float(methodPrice) * data['shirinaZabora'] * data['dlinaZabora'] * visota)})
    delivery = 3000
    data['kmMkad'] = float(data['kmMkad'])
    if int(data['kmMkad']) > 30:
         delivery = delivery + 65 * (int(data['kmMkad']) - 30)
    args['result_items'].append({'text': f"Доставка {int(data['kmMkad'])} км от МКАД", 'cost': delivery})
    print('----------------')
    print(args)
    return args