def main(args, data, param, descrs):
    stolb_count = {'3': 4, '4': 6, '5': 6, '6': 6, '7': 8, '8': 8, '9': 8, '10': 10, '11': 10, '12': 10, '13': 12, '14': 12, '15': 12, '16': 14, '17': 14, '18': 14, '19': 16, '20': 16}
    stolb_count = stolb_count[data['dlinaZabora']]
    stolb_price = ''
    answer = [
        {'text': f'Столбы профильные: {stolb_count} шт.', 'cost': stolb_count * stolb_price}
    ]

    return None