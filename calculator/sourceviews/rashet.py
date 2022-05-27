

def main(args, data, filename, names):
    args['result'] = 0.0
    args['result_items'] = []

    if 'dlinaZabora' not in data.keys():
        data['dlinaZabora'] = 1
    else:
        data['dlinaZabora'] = float(data['dlinaZabora'])

    if 'visotaZabora' not in data.keys():
        data['visotaZabora'] = 1
    else:
        data['visotaZabora'] = float(data['visotaZabora'])

    if 'shirinaZabora' not in data.keys():
        data['shirinaZabora'] = 1
    else:
        data['shirinaZabora'] = float(data['shirinaZabora'])
    ploshad = data['dlinaZabora'] * data['visotaZabora'] * data['shirinaZabora']
    for inp in data.keys():
        if filename + inp.lower() in args.keys():
            obj = args[filename + inp.lower()]
            desc = names[filename + inp.lower()]
            for i in obj:
                if 'start' in i.keys():
                    if i['start'] <= float(data[inp]) <= i['end']:
                        args['result_items'].append(
                            {'text': f"{desc}", 'cost': int((float(data[inp]) * float(i['mnosh'])) + float(i['price']))})
                        args['result'] += int((float(data[inp]) * float(i['mnosh'])) + float(i['price']))
                else:
                    if str(i['value']) == str(data[inp]):
                        try:
                            data[inp] = int(data[inp])
                            i['value'] = int(i['value'])
                            args['result_items'].append(
                                    {'text': f"{desc}",
                                     'cost': int((float(data[inp]) * float(i['mnosh'])) + float(i['price']))})
                            args['result'] += int((float(data[inp]) * float(i['mnosh'])) + float(i['price']))
                        except:
                            pass

    args['result'] = int(args['result'])
    return args
