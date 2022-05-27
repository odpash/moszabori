from django.shortcuts import render
from home.models import *
from .models import Services, ServiceCategory

from django.core.mail import send_mail 
from django.shortcuts import redirect 
# from django.core import mail
# Create your sourceviews here.

def homePage(request):
    # tours = Tour.objects.all().order_by('-id')[:4]
    # posts = Post.objects.all().order_by('-id')[:4]
    zaborCategories = ServiceCategory.objects.all() # # used to show other categories
    portfolioList = Portfolio.objects.all()[:6]
    SEO = SEO_Optimiser.objects.get(seoid=1)
    args = {
            'SEO': SEO,
            'zaborCategories': zaborCategories,
            # 'posts': posts,
            'portfolioList': portfolioList,
        }
    return render(request, 'home/index.html', args)

def aboutUs(request):
    page = Page.objects.get(pageid=4) #Look in admin for the page id
    template = 'home/about-us.html'
    SEO = page.SEO
    args = {
        'page': page,
        'SEO': SEO,
    }
    return render(request, template, args) #


def viezdZamershika(request):
    template = 'home/viezd-zamershika.html'
    return render(request, template)



def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name') if request.POST.get('name') != None else ''
        phone = request.POST.get('phone') if request.POST.get('phone') != None else ''
        email = request.POST.get('email') if request.POST.get('email') != None else ''
        subject = request.POST.get('subject') if request.POST.get('subject') != None else ''
        message = request.POST.get('message') if request.POST.get('message') != None else ''

        fromEmail = 'info@moszn.ru'
        toEmail = 'info@moszn.ru'

        finalMessage = 'Здравствуйте!!\n\nПосетитель вашего сайта -  '+str(name)+\
            'отправил вам сообщеине: \n\
            Имя: '+ str(name) + '\n\
            Email: '+ str(email) + '\n\
            Телефон: ' + str(phone) + '\n\
            Тема: ' + str(subject) + '\n\
            Сообщение:' +str(message)+ '\n\n\
            Пожалуйста ответьте на его сообщение как можно скорее.\n\n\
            С уважением,\n\nМосковские Заборы и Навесы'

        subject = "Новое сообщение от " + str(name) 
        send_mail(subject, finalMessage, fromEmail, (toEmail,), fail_silently=False,)
        # return redirect('home:contacts')
        args = {
                # 'tours': Tour.objects.order_by('-Created')[:3],
            }
        return render(request, 'home/mail-sent-success.html', args)

        
    page = Page.objects.get(pageid=6) 
    SEO = page.SEO
    template = 'home/contacts.html'

    # SEO = SEO_Optimiser.objects.get(seoid=5)
    args = {
        'page': page,
        'SEO': SEO,
    }
    return render(request, template, args) #

def FAQs(request):
    # SEO = SEO_Optimiser.objects.get(seoid=1)
    page = Page.objects.get(pageid=1)
    SEO = page.SEO
    FAQs = FAQ.objects.all()

    args = {
            'SEO': SEO,
            'page': page,
            'FAQs': FAQs,
            }
    return render(request, 'home/faq.html', args) 


def pricelist(request):
    page = Page.objects.get(pageid=5) 
    template = 'home/pricelist.html'
    SEO = page.SEO
    # SEO = SEO_Optimiser.objects.get(seoid=4)
    pricelist = Pricelist.objects.all()

    args = {
        'page': page,
        'SEO': SEO,
        'pricelist': pricelist,
    }
    return render(request, template, args) #


def zaborCategoryList(request):
    # page = Page.objects.get(pageid=1) 
    template = 'home/zabory_categories_list.html'
    # SEO = page.SEO
    SEO = SEO_Optimiser.objects.get(seoid=2)
    # zabory = Services.objects.filter(status='published')
    zaborCategories = ServiceCategory.objects.all()
    page = Page.objects.get(pageid=3) 

    args = {
        'page': page,
        'SEO': SEO,
        # 'zabory': zabory,
        'zaborCategories': zaborCategories, 
    }
    return render(request, template, args) 

def zaborCategory(request, Slug):
    # page = Page.objects.get(pageid=1) 
    template = 'home/zabor_category.html'
    # SEO = SEO_Optimiser.objects.get(seoid=2)
    # navesy = Naves.objects.filter(status='published')
    zaborCategory = ServiceCategory.objects.get(Slug=Slug)
    zabory = Services.objects.filter(status='published', Category=zaborCategory.id)

     
    zaborCategories = ServiceCategory.objects.all() # # used to show other categories

    args = {
        'zabory': zabory,
        'zaborCategory': zaborCategory,
        'zaborCategories': zaborCategories, # used to show other categories
    }
    return render(request, template, args) #

def zaborDetails(request, Slug):
    zabor = Services.objects.get(Slug=Slug)
    services = Services.objects.filter(Category=zabor.Category)

    args = {
        'service' : zabor,
        'services': services,
        'obj': zabor,

    }

    if request.method == 'POST':
        recipient_name = request.POST.get("recipient-name", "")
        recipient_phone = request.POST.get("recipient-phone", "")
        recipient_email = request.POST.get("recipient-email", "")

        zakazObj = zabor
        fromCompany = 'info@moszn.ru' 
        reciever_list= ('info@moszn.ru',) 
        subject = 'Новый заказ  - '+ str(zakazObj.Title) + ' от '+ recipient_name 
        message = "Новый запрос на ваш товар - "+ str(zakazObj.Title)+ \
            "(https://naves.ru"+str(request.path) + "). \n\n" \
            "Детали товара:\n" \
            "\nНазвание: "+ str(zakazObj.Title) \
            +"\nURL: https://naves.ru"+str(request.path) \
            + "\n\nЗАКАЗЧИК:\n" \
            +"\nИмя: "+str(recipient_name)  \
            + "\nТелефон: "+ str(recipient_phone) \
            + "\nEmail: " + str(recipient_email)  \
            + " \n\n" \
            + "С уважением,\n\nМосковские Заборы и Навесы"
        # try:
        send_mail(subject, message, fromCompany, reciever_list, fail_silently=False, )
        template = 'home/spasibo-za-zakaz.html'
        return render(request, template, args)
    
    return render(request, 'home/zabor-details.html', args)




def navesy(request):
    # page = Page.objects.get(pageid=1) 
    template = 'home/navesy.html'
    # SEO = page.SEO
    SEO = SEO_Optimiser.objects.get(seoid=2)
    navesy = Naves.objects.filter(status='published')
    navesCategories = NavesCategory.objects.all()
    page = Page.objects.get(pageid=2) 



    args = {
        # 'page': page,
        'SEO': SEO,
        'navesy': navesy,
        'navesCategories': navesCategories,
        'page': page,
        

    }
    return render(request, template, args) #

def navesCategory(request, Slug):
    # page = Page.objects.get(pageid=1) 
    template = 'home/navesy-category.html'
    # SEO = SEO_Optimiser.objects.get(seoid=2)
    # navesy = Naves.objects.filter(status='published')
    navesCategory = NavesCategory.objects.get(Slug=Slug)
    navesy = Naves.objects.filter(status='published', Category=navesCategory.id)

     
    navesCategories = NavesCategory.objects.all()

    args = {
        'navesy': navesy,
        'navesCategory': navesCategory,
        'navesCategories': navesCategories, # used to show other categories
    }
    return render(request, template, args) #

def navesDetails(request, Slug):
    template = 'home/naves-details.html'
    naves = Naves.objects.get(Slug=Slug)
    navesCategory = NavesCategory.objects.get(id=naves.id)
    # navesy = Naves.objects.filter(status='published', Category=navesCategory.id)
    
    navesCategories = NavesCategory.objects.all()

    args = {
        'naves': naves,
        'obj': naves,
        'navesCategory': navesCategory,
        'navesCategories': navesCategories, # used to show other categories
    }

    if request.method == 'POST':
        recipient_name = request.POST.get("recipient-name", "")
        recipient_phone = request.POST.get("recipient-phone", "")
        recipient_email = request.POST.get("recipient-email", "")

        zakazObj = naves
        fromCompany = 'info@moszn.ru' 
        reciever_list= ('info@moszn.ru',) 
        subject = 'Новый заказ  - '+ str(zakazObj.Title) + ' от '+ recipient_name 
        message = "Новый запрос на ваш товар - "+ str(zakazObj.Title)+ \
            "(https://naves.ru"+str(request.path) + "). \n\n" \
            "Детали товара:\n" \
            "\nНазвание: "+ str(zakazObj.Title) \
            +"\nURL: https://naves.ru"+str(request.path) \
            + "\n\nЗАКАЗЧИК:\n" \
            +"\nИмя: "+str(recipient_name)  \
            + "\nТелефон: "+ str(recipient_phone) \
            + "\nEmail: " + str(recipient_email)  \
            + " \n\n" \
            + "С уважением,\n\nМосковские Заборы и Навесы"
        # try:
        send_mail(subject, message, fromCompany, reciever_list, fail_silently=False, )
        template = 'home/spasibo-za-zakaz.html'
        return render(request, template, args)

    return render(request, template, args) #

def obratniyZvonok(request):
    template = 'home/zvonok.html'

    args = {}

    if request.method == 'POST':
        recipient_name = request.POST.get("recipient-name", "")
        recipient_phone = request.POST.get("recipient-phone", "")
        fromCompany = 'info@moszn.ru' 
        reciever_list= ('info@moszn.ru',) 
        subject = 'Заказ звонка от '+ recipient_name 
        message = "Посетитель вашего сайта -  "+str(recipient_name)  \
            + " хочет чтобы вы позвонили ему на номер: "+str(recipient_phone) +"\n\n" \
            + "\n\nМосковские Заборы и Навесы"
        # try:
        send_mail(subject, message, fromCompany, reciever_list, fail_silently=False, )
        return render(request, template, args)
        


    return render(request, template, args) #



def portfolio(request):
    # page = Page.objects.get(pageid=1) 
    template = 'home/portfolio.html'
    # SEO = page.SEO
    SEO = SEO_Optimiser.objects.get(seoid=3)
    portfolioList = Portfolio.objects.all()

    portfolioCategories = PortfolioCategory.objects.all()

    args = {
        # 'page': page,
        'SEO': SEO,
        'portfolioList': portfolioList,
        'portfolioCategories': portfolioCategories,
    }
    return render(request, template, args) #


def portfolioDetails(request, Slug):
    
    portfolio = Portfolio.objects.get(Slug=Slug)
    context = {
        'portfolio' : portfolio,
        'obj': portfolio,

    }
    return render(request, 'home/portfolio-details.html',context)





