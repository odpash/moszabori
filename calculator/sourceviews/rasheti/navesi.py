def main(args, data):
    args['result'] = 0.0  # result value
    args['result_items'] = []
    data['shirinaZabora'] = int(float(data['shirinaZabora']))
    data['dlinaZabora'] = int(float(data['dlinaZabora']))
    visota = float(data['visotaZabora'])

    fermiPrice = [i['price'] for i in args['Navesifermi'] if i['value'] == data['fermi']][0]

    args['result_items'].append({'text': 'Боковая ферма', 'cost': data['dlinaZabora'] * int(data['fermi']) * int(fermiPrice)})
    args['result_items'].append({'text': "Покраска цветной эмалью 3 в 1 Dali столбов, обрешетки и фермы", 'cost': 400 * data['dlinaZabora'] * data['shirinaZabora']})


    methodPrice = [i['price'] for i in args['Navesimethod'] if i['value'] == data['method']][0]
    args['result_items'].append({'text': data['method'], 'cost': float(methodPrice) * data['shirinaZabora'] * data['dlinaZabora'] * visota})
    delivery = 3000
    data['kmMkad'] = float(data['kmMkad'])
    if int(data['kmMkad']) > 30:
         delivery = delivery + 65 * (int(data['kmMkad']) - 30)
    args['result_items'].append({'text': f"Доставка {data['kmMkad']} км от МКАД", 'cost': delivery})
    print('----------------')
    print(args)
    return args