from django.shortcuts import render
from home.models import SEO_Optimiser
from calculator.sourcemodels.profnastil import *
import math
from decimal import Decimal


def main(request):
    # page = Page.objects.get(pageid=1) #Look in admin for the page id
    global kalitokMaterialPrice, tipPokritiyaMaterialCost, vorotMaterialPrice, utrambovkaMaterialCost, stolbiMaterialCost, lagMaterialCost, samorezMaterialCost, zaglushkaMaterialCost
    template = 'calculator/profnastil.html'
    SEO = SEO_Optimiser.objects.get(seoid=6)
    # pokritiya = Pokritie.objects.select_related().values('Title')
    dlinaZabora = Decimal(request.GET.get('dlinaZabora', 0.0))
    visotaZabora = Decimal(request.GET.get('visotaZabora', 0.0))

    betonirovanieLaborCost = 0
    gruntovkaMaterialCost = 0
    totalMaterialCost = 0
    totalLaborCost = 0
    plankaMaterialCost = 0
    kraskaMaterialCost = 0

    messages = ''

    status = 0
    if request.GET.get('dlinaZabora') is not None:
        status = 1

    if dlinaZabora != None and visotaZabora != None:
        ploshadZabora = dlinaZabora * visotaZabora

        # 2. Stolba narkhat nawi viray
        # 2.1 Yakum, stolba object viray, lak wam narkh fam
        userSechStolb = request.GET.get('sechenieStolbcov', '')
        # userTolshStolb = request.GET.get('tolshinaStolbcov', '')
        userTolshStolb = request.GET.get('tolshinaStolbcov', 1.5)
        print(userSechStolb)
        print(userTolshStolb)
        if userSechStolb != '' and userTolshStolb != '':
            try:
                stolbaObj = ProfnastilStolba.objects.get(sechenieStolba__Title=userSechStolb,
                                                         tolshinaStolba__Title=userTolshStolb)
                print('Solba success')
            except:
                stolbaObj = ProfnastilStolba.objects.get(sechenieStolba__Title='80x80',
                                                         tolshinaStolba__Title='2.0')
                print('Solba failed: except block running')

                messages += """Сечение и/или толшина столбы не выбран; по умолчанию выбрали 80х80х2.0 """
        else:
            print("Сечение и/или толшина столбы не выбран; по умолчанию выбрали 80х80х2.0 ")
            stolbaObj = ProfnastilStolba.objects.get(sechenieStolba__Title='80x80',
                                                     tolshinaStolba__Title='2.0')
            # messages += """Сечение и/или толшина столбы не выбран; по умолчанию выбрали 80х80х2.0 """

        print(stolbaObj.tipStolba, stolbaObj.sechenieStolba.Title, stolbaObj.tolshinaStolba)
        # try:
        #     stolbaObj = Stolba.objects.get(sechenieStolba__Title=userSechStolb,
        #                                     tolshinaStolba__Title=userTolshStolb)
        #     print("Sechenie su")
        # except:
        #     stolbaObj = Stolba.objects.get(sechenieStolba__Title='60x60',
        #                                     tolshinaStolba__Title='1.5')
        #     messages += """Выбранный вам сечения или толщина столбы не найден. по умолчанию, мы выбрали столба размером 60х60х1.5"""
        # else:
        #     # you can raise an eroor here if either or both are none
        #     # For now, get default if not set
        #     stolbaObj = Stolba.objects.get(sechenieStolba__Title='60x60',
        #                                         tolshinaStolba__Title='1.5')
        # messages += """Выбранный вам сечения или толщина столбы не найден. по умолчанию, мы выбрали столба размером 60х60х1.5"""

        # Shag viray
        shagStolbcov = Decimal(request.GET.get('shagStolbcov', 2.5))

        zaglublenieStolba = Decimal(request.GET.get('zaglublenieStolba', 1.2))
        print('zaglublenieStolba: ', zaglublenieStolba)
        oneStolbLength = visotaZabora + zaglublenieStolba
        print('oneStolbLength: ', oneStolbLength)

        # find stolbCounter, i.e. how many oneStolbLength (means final calulated length of stolb) we need?
        if shagStolbcov:  # != None:
            stolbCounter = math.ceil(dlinaZabora / shagStolbcov)
        else:
            # if solbKolichestvo not set, set it as 2
            stolbCounter = (dlinaZabora / 2)

        stolbiMaterialCost = oneStolbLength * stolbCounter * stolbaObj.cena  #
        # stolbLaborCost  = stolbCounter *
        # founded total price of the stolbi
        totalMaterialCost += stolbiMaterialCost
        # Ustanovka Stolbi
        graviyLaborCostObj = ProfnastilLaborCost.objects.get(Slug='graviy')
        graviyLaborCost = stolbCounter * graviyLaborCostObj.cena

        totalLaborCost += graviyLaborCost

        # 2. Lag price find
        lagCounter = int(request.GET.get('lag', 2))
        # find lag price
        # TO CALCULATE THE EXACT LAG PRICE, A USER NEEDS TO SELECT THE LAG TYPE (!?)
        # OR how to select lag type
        lagObj = ProfnastilServicesAndMaterials.objects.get(Slug='lagi40x20x020')
        lagMaterialCost = dlinaZabora * Decimal(1.1) * Decimal(lagCounter) * Decimal(
            lagObj.cena)  # cena baghay decimal vawde...
        totalMaterialCost += lagMaterialCost

        # find samorez price based on lag
        samorezObj = ProfnastilServicesAndMaterials.objects.get(Slug='samorezCink')
        if lagCounter == 2:
            samorezCounter = dlinaZabora * 8
        elif lagCounter == 3:
            samorezCounter = dlinaZabora * 12

        samorezMaterialCost = samorezCounter * samorezObj.cena
        totalMaterialCost += samorezMaterialCost

        # ZAGLUSHKA COSTS
        stolbSechenie = str(stolbaObj.sechenieStolba.Title)
        print('stolbSechenie=' + stolbSechenie)

        # if stolbaObj:
        #     try:
        #         sech = stolbaObj.sechenieStolba.Title
        #         zaglushkaObjs = ServicesAndMaterials.objects.filter(smtip='zaglushka').get(param1=sech)
        #         print('Zaglushka selection success')
        #     except:
        #         print('Failed Zaglushka selection')
        #         # zaglushkaObj = ServicesAndMaterials.objects.filter(smtip='zaglushka').get(param1='80x80')
        #         zaglushkaObj = ServicesAndMaterials.objects.filter(smtip='zaglushka').get(param1='80х80')

        try:
            zaglushkaObjs = ProfnastilServicesAndMaterials.objects.filter(smtip='zaglushka')
            print(zaglushkaObjs)
            # zaglushkaObj = zaglushkaObjs.get(param1=stolbSechenie)
            getZagSlug = 'zaglushka' + str(stolbSechenie)
            print(getZagSlug)
            # zaglushkaObj = zaglushkaObjs.get(Slug=getZagSlug)
            sech = str(stolbaObj.sechenieStolba.Title)
            print(sech)
            for obj in zaglushkaObjs:
                print(obj.param1)

            # zaglushkaObj = zaglushkaObjs.get(param1=sech)
            zaglushkaObj = ProfnastilServicesAndMaterials.objects.filter(smtip='zaglushka').get(param1=sech)

            print('zaglushkaObj success:', zaglushkaObj)

        except:
            print('Failed Zaglushka')
            zaglushkaObj = ProfnastilServicesAndMaterials.objects.filter(smtip='zaglushka').get(param1='80х80')
            # zaglushkaObj = ServicesAndMaterials.objects.filter(smtip='zaglushka').get(param1=stolbSechenie)

            print('Выбран заглушка 80х80 по умолчанию.')
            messages += '''Выбран заглушка 80х80 по умолчанию. '''

        zaglushkaMaterialCost = zaglushkaObj.cena * stolbCounter
        totalMaterialCost += zaglushkaMaterialCost

        # # # get the type of planke
        # for zObj in zaglushkiObjects:
        #     print('zObj.param1',zObj.param1)
        #     print('stolbSechenie', stolbSechenie)
        #     if zObj.param1 == stolbSechenie:
        #         print('True')
        #         zaglushkaObj = ServicesAndMaterials.objects.get(param1=stolbSechenie)
        #         print(zaglushkaObj.Title)

        betonirovanie = request.GET.get('betonirovanie')

        if betonirovanie == '1':
            betonObj = ProfnastilServicesAndMaterials.objects.get(Slug='betonirovanie')
            betonirovanieMaterialCost = stolbCounter * Decimal(betonObj.cena)
            totalMaterialCost += betonirovanieMaterialCost

            # find the laborCost for betonirovanie
            betonLaborObj = ProfnastilLaborCost.objects.get(Slug='betonirovanie')
            betonirovanieLaborCost = stolbCounter * betonLaborObj.cena
            totalLaborCost = totalLaborCost + betonirovanieLaborCost


        else:
            betonirovanieMaterialCost = 0

        utrambovka = request.GET.get('utrambovka')

        if utrambovka == '1':
            utrambovkaObj = ProfnastilServicesAndMaterials.objects.get(Slug='utrambovka')
            utrambovkaMaterialCost = stolbCounter * Decimal(utrambovkaObj.cena)
            totalMaterialCost += utrambovkaMaterialCost
        else:
            utrambovkaMaterialCost = 0

        gruntovkaID = request.GET.get('gruntovka')
        if gruntovkaID != '0':
            try:
                gruntovkaObj = ProfnastilServicesAndMaterials.objects.get(Slug="gruntovka")

                gruntovkaMaterialCost = dlinaZabora * Decimal(gruntovkaObj.cena)
                totalMaterialCost += gruntovkaMaterialCost


            except:
                messages += '''\nГрунтовка не рассчитан '''

        kraskaID = request.GET.get('kraska', 'no')
        if kraskaID != 'no':
            kraska = ProfnastilKraska.objects.get(id=kraskaID)

            kraskaMaterialCost = kraska.cena * ploshadZabora
            totalMaterialCost += kraskaMaterialCost
        else:
            kraskaMaterialCost = 0

        tipPokritiyaID = request.GET.get('tipPokritiya', '')
        if tipPokritiyaID != '':
            tipPokritiyaObj = ProfnastilPokritie.objects.get(id=tipPokritiyaID)

            tipPokritiyaMaterialCost = Decimal(tipPokritiyaObj.cena) * ploshadZabora
            totalMaterialCost += tipPokritiyaMaterialCost

            # PLANKI MATERIAL COST
            pokKod = str(tipPokritiyaObj.get_marka_display()) + str(tipPokritiyaObj.get_kolVolna_display())
            # print(pokKod)
            planki = ProfnastilServicesAndMaterials.objects.filter(smtip='planka')

            # get the type of planka
            for obj in planki:
                if obj.param1 == pokKod:
                    planka = planki.get(param1=pokKod)
                    print("Выбран планка: ", planka)

            plankaMaterialCost = Decimal(dlinaZabora) * Decimal(1.1) * planka.cena
            totalMaterialCost += plankaMaterialCost

            # USTANOVKA PROFNASTILA LABOR COST
            ustZabProfObjects = ProfnastilLaborCost.objects.filter(workType='ustZaborProfnast').order_by('param1')

            def getUstanovkaProfLaborCost(objs, visotaZabora):
                objAvlHeights = []
                for obj in objs:
                    objAvlHeights.append(obj.param1)

                # objAvlHeights = LaborCost.objects.filter(workType='ustZaborProfnast').values_list('param1', flat=True).distinct()
                objAvlHeights.sort()  # filtered list
                print(objAvlHeights)  # [ 1, 4, 5, 7, 8 ]

                minHeight = 0
                maxHeight = 0
                optimalHeight = 0  # need to be 1.7

                # objAvlHeights = [ 1.5, 1.7 ]
                visotaZabora = Decimal(visotaZabora)  # 2.0
                for item in objAvlHeights:
                    item = Decimal(item)
                    if item < visotaZabora:
                        minHeight = item  # 1.5
                        optimalHeight = minHeight  # 1.5
                    elif item == visotaZabora:
                        optimalHeight = visotaZabora
                        break
                    else:
                        maxHeight = item  # 7
                        optimalHeight = maxHeight
                        break

                print(optimalHeight)

                ustZabProfObj = ProfnastilLaborCost.objects.filter(workType='ustZaborProfnast').get(
                    param1=optimalHeight)
                print(ustZabProfObj.param1)
                ustZaborLaborCostResult = ustZabProfObj.cena * dlinaZabora
                print('Custom inner func success!')
                return ustZaborLaborCostResult
                # end of inner func

            # print(getUstanovkaProfLaborCost(ustZabProfObjects, visotaZabora))
            try:
                ustZaborLaborCost = getUstanovkaProfLaborCost(ustZabProfObjects, visotaZabora)
                print('ustZaborLaborCost', ustZaborLaborCost)
                totalLaborCost += ustZaborLaborCost
                print('ustZaborLaborCost calc success')
            except:
                ustZaborLaborCost = 0
                messages += '''Стоимость работы установки забора не рассчитан. '''

        else:  # if no tipPokritiyaID
            tipPokritiyaMaterialCost = 0
            pokKod = 0
            ustZaborLaborCost = 0

            # VOROT
            # 1) LABOR AND
            # 2) MATERIAL COST
        vorotCounter = int(request.GET.get('kolVorot', 0))
        if vorotCounter and int(vorotCounter) > 0:

            # find width and height and then the price
            shirinaVorot = request.GET.get('shirinaVorot', 0)
            visotaVorot = request.GET.get('visotaVorot', 0)
            if shirinaVorot != '' and visotaVorot != '':
                # print(shirinaVorot, visotaVorot)
                try:
                    vorotObj = ProfnastilServicesAndMaterials.objects.filter(smtip='vorota').get(param2=visotaVorot,
                                                                                                 param1=shirinaVorot)
                    vorotMaterialPrice = vorotObj.cena * vorotCounter
                    totalMaterialCost += vorotMaterialPrice
                    vorotLaborCost = ProfnastilLaborCost.objects.get(Slug='ustKarkasVorotKalit').cena * vorotCounter
                    totalLaborCost += vorotLaborCost
                except:
                    messages += '''\nСтоимость ворот не рассчитан. Не выбран ширина или высота ворот '''
                    vorotMaterialPrice = 0
        else:
            vorotMaterialPrice = 0
            vorotLaborCost = 0

        # KALITKA PART
        kalitokCounter = int(request.GET.get('kolKalitok', 0))
        if kalitokCounter and kalitokCounter > 0:

            # find width and height and then the price
            shirinaKolitok = request.GET.get('shirinaKolitok', 0)
            visotaKolitok = request.GET.get('visotaKolitok', 0)
            if shirinaKolitok != '' and visotaKolitok != '':
                try:
                    kalitkaObj = ProfnastilServicesAndMaterials.objects.filter(smtip='kalitka').get(
                        param2=visotaKolitok, param1=shirinaKolitok)

                    # find Kalitok material cost and add to the totalLaborCost
                    kalitokMaterialPrice = kalitkaObj.cena * kalitokCounter
                    totalMaterialCost += kalitokMaterialPrice

                    # find Kalitok labor cost and add to the totalLaborCost
                    kalitokLaborCost = ProfnastilLaborCost.objects.get(Slug='ustKarkasVorotKalit').cena * kalitokCounter
                    totalLaborCost += kalitokLaborCost
                except:
                    messages += '''\n\nКалитка не рассчитан. Не все данные были введены!'''

        else:
            kalitokMaterialPrice = 0
            kalitokLaborCost = 0

    else:  # if no dlinaZabora == ? or no visotaZabora == ?
        ploshadZabora = 0
        betonirovanieMaterialCost = 0
    totalCost = int(totalLaborCost + totalMaterialCost)

    # These initial data is used to fill the form
    pokritiya = ProfnastilPokritie.objects.all()
    kraski = ProfnastilKraska.objects.all()
    visotaVorot = ProfnastilServicesAndMaterials.objects.filter(smtip='vorota').values_list('param2',
                                                                                            flat=True).distinct()  # values('param1')
    shirinaVorot = ProfnastilServicesAndMaterials.objects.filter(smtip='vorota').values_list('param1',
                                                                                             flat=True).distinct()
    visotaKalitok = ProfnastilServicesAndMaterials.objects.filter(smtip='kalitka').values_list('param2',
                                                                                               flat=True).distinct()  # values('param1')
    shirinaKalitok = ProfnastilServicesAndMaterials.objects.filter(smtip='kalitka').values_list('param1',
                                                                                                flat=True).distinct()

    # This will return a queryset. So to view this:
    # visotaVorot.values() #returns a list of objects(dicts)

    args = {
        # 'page': page,
        'SEO': SEO,
        'messages': messages,
        'status': status,

        # LABOR COST
        'graviyLaborCost': graviyLaborCost,
        'kalitokLaborCost': kalitokLaborCost,
        'vorotLaborCost': vorotLaborCost,
        'ustZaborLaborCost': ustZaborLaborCost,
        'betonirovanieLaborCost': betonirovanieLaborCost,
        'totalLaborCost': totalLaborCost,

        # Material COST
        'vorotMaterialPrice': vorotMaterialPrice,
        'kalitokMaterialPrice': kalitokMaterialPrice,
        'tipPokritiyaMaterialCost': tipPokritiyaMaterialCost,
        'betonirovanieMaterialCost': int(betonirovanieMaterialCost),
        'utrambovkaMaterialCost': utrambovkaMaterialCost,
        'stolbiMaterialCost': int(stolbiMaterialCost),
        'lagMaterialCost': lagMaterialCost,
        'totalMaterialCost': int(totalMaterialCost),
        'zaglushkaMaterialCost': zaglushkaMaterialCost,
        'samorezMaterialCost': samorezMaterialCost,
        'gruntovkaMaterialCost': gruntovkaMaterialCost,
        'plankaMaterialCost': plankaMaterialCost,
        'kraskaMaterialCost': kraskaMaterialCost,
        'totalCost': totalCost,

        # Additional parameter for FORM get
        'stolbaObj': stolbaObj,
        'visotaKalitok': visotaKalitok,
        'shirinaKalitok': shirinaKalitok,
        'visotaVorot': visotaVorot,
        'shirinaVorot': shirinaVorot,
        'tipPokritiyaID': tipPokritiyaID,
        'pokKod': pokKod,
        'stolbSechenie': stolbSechenie,
        'dlinaZabora': dlinaZabora,
        'visotaZabora': visotaZabora,
        'ploshadZabora': Decimal(ploshadZabora),
        # 'zaglushkiObjects': zaglushkiObjects,
        'pokritiya': pokritiya,
        'kraski': kraski,

        'oneStolbLength': oneStolbLength,
        'stolbCounter': stolbCounter,
        'shagStolbcov': shagStolbcov,

        'zaglushkaObj': zaglushkaObj,
        'lagObj': lagObj
        # 'pokritiya_as_json': pokritiya #json.dumps(list(pokritiya)),

    }
    rrr = []
    try:
        rrr.append({'text': 'Цена ворот', 'cost': int(vorotMaterialPrice), 'count': int(vorotCounter), 'ed': 'шт.',
                    'price': round(vorotMaterialPrice / vorotCounter, 2)})
    except:
        pass
    try:
        rrr.append(
            {'text': 'Цена калитки', 'cost': int(kalitokMaterialPrice), 'count': int(kalitokCounter), 'ed': 'шт.',
             'price': round(kalitokMaterialPrice / kalitokCounter, 2)})
    except:
        pass
    try:
        rrr.append({'text': 'Цена калитки', 'cost': int(vorotMaterialPrice), 'count': int(vorotCounter), 'ed': 'шт.',
                    'price': round(vorotMaterialPrice / vorotCounter, 2)})
    except:
        pass
    try:
        rrr.append({'text': 'Покрытие', 'cost': int(tipPokritiyaMaterialCost), 'count': int(ploshadZabora), 'ed': 'шт.',
                    'price': round(tipPokritiyaMaterialCost / ploshadZabora, 2)})
    except:
        pass
    try:
        rrr.append(
            {'text': 'Бетонирование', 'cost': int(betonirovanieMaterialCost), 'count': int(stolbCounter), 'ed': 'шт.',
             'price': round(betonirovanieMaterialCost / stolbCounter, 2)})
    except:
        pass
    try:
        rrr.append({'text': 'Утрамбовка', 'cost': int(utrambovkaMaterialCost), 'count': int(stolbCounter), 'ed': 'шт.',
                    'price': round(utrambovkaMaterialCost / stolbCounter, 2)})
    except:
        pass
    try:
        rrr.append(
            {'text': 'Столб. материалы', 'cost': int(stolbiMaterialCost), 'count': int(oneStolbLength * stolbCounter),
             'ed': 'шт.',
             'price': round(stolbiMaterialCost / (oneStolbLength * stolbCounter), 2)})
    except:
        pass
    try:
        rrr.append({'text': 'Лаг материалы', 'cost': int(lagMaterialCost),
                    'count': int(dlinaZabora * Decimal(1.1) * Decimal(lagCounter)), 'ed': 'шт.',
                    'price': round(lagMaterialCost / (dlinaZabora * Decimal(1.1) * Decimal(lagCounter)), 2)})
    except:
        pass
    try:
        rrr.append({'text': 'Заглушки', 'cost': int(zaglushkaMaterialCost), 'count': int(stolbCounter), 'ed': 'шт.',
                    'price': round(zaglushkaMaterialCost / stolbCounter, 2)})
    except:
        pass
    try:
        rrr.append({'text': 'Саморез', 'cost': int(samorezMaterialCost), 'count': int(samorezCounter), 'ed': 'шт.',
                    'price': round(samorezMaterialCost / samorezCounter, 2)})
    except:
        pass
    try:
        rrr.append({'text': 'Грунтовка', 'cost': int(gruntovkaMaterialCost), 'count': int(dlinaZabora), 'ed': 'шт.',
                    'price': round(gruntovkaMaterialCost / dlinaZabora, 2)})
    except:
        pass
    try:
        rrr.append(
            {'text': 'Планка', 'cost': int(plankaMaterialCost), 'count': int(Decimal(dlinaZabora) * Decimal(1.1)),
             'ed': 'шт.',
             'price': round(plankaMaterialCost / (Decimal(dlinaZabora) * Decimal(1.1)), 2)})
    except:
        pass
    try:
        rrr.append({'text': 'Краска', 'cost': int(kraskaMaterialCost), 'count': int(ploshadZabora), 'ed': 'шт.',
                    'price': round(kraskaMaterialCost / ploshadZabora, 2)})
    except:
        pass

    args['result_items'] = []
    args['result_ysl'] = []
    args['result_dos'] = []
    args['result_items_a'] = [{
        'text': "Итого за материалы:", 'cost': str(round(totalMaterialCost, 2)) + " руб."
    }]
    args['result'] = totalCost
    for i in rrr:
        if int(i['cost']) > 0:
            i['cost'] = str(i['cost']) + " руб."
            i['count'] = str(i['count']) + ' шт.'
            i['price'] = str(i['price']) + " руб."
            args['result_items'].append(i)

    rrr2 = [{'text': 'Установка столбов', 'cost': graviyLaborCost, 'count': int(stolbCounter), 'ed': 'шт.',
             'price': round(graviyLaborCost, 2)},
            {'text': 'Устновка калиток', 'cost': kalitokLaborCost, 'count': int(kalitokCounter), 'ed': 'шт.',
             'price': round(ProfnastilLaborCost.objects.get(Slug='ustKarkasVorotKalit').cena, 2)},
            {'text': 'Установка ворот', 'cost': vorotLaborCost, 'count': int(vorotCounter), 'ed': 'шт.',
             'price': round(ProfnastilLaborCost.objects.get(Slug='ustKarkasVorotKalit').cena, 2)}]
    try:
        rrr2.append({'text': 'Бетонирование', 'cost': betonirovanieLaborCost, 'count': int(stolbCounter), 'ed': 'шт.',
                     'price': round(betonirovanieLaborCost / stolbCounter, 2)})
    except:
        pass
    try:
        rrr2.append({'text': 'Установка забора', 'cost': ustZaborLaborCost, 'count': int(dlinaZabora), 'ed': 'шт.',
                     'price': round(ustZaborLaborCost / dlinaZabora, 2)})
    except:
        pass
    args['result_ysl_a'] = [{
        'text': "Итого за услуги:", 'cost': str(round(totalLaborCost, 2)) + " руб."
    }]
    for i in rrr2:
        if int(i['cost']) > 0:
            i['cost'] = str(i['cost']) + " руб."
            i['count'] = str(i['count']) + ' шт.'
            i['price'] = str(i['price']) + " руб."
            print(i)
            args['result_ysl'].append(i)
    try:
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
    except:
        pass
    args['result'] = str(args['result']) + " руб."
    return render(request, template, args)  # last arg: args
