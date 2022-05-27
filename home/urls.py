from django.contrib import admin
from django.urls import path,  include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
admin.site.site_header = "Московский заборы и навесы"

urlpatterns = [ 
    path('', views.homePage, name='homePage'), 
    path('about-us', views.aboutUs, name="aboutUs"),
    path('viezd-zamershika', views.viezdZamershika, name="viezd-zamershika"),

    path('zabory/', views.zaborCategoryList, name="zaborCategoryList"),
    path('zabory/category/<slug:Slug>', views.zaborCategory, name='zaborCategory'),
    path('zabory/<slug:Slug>', views.zaborDetails, name='zaborDetails'),
    

    path('navesy/', views.navesy, name="navesy"), # page Navesy; 
    # navesCategory - sourceviews info about naves category and lists the navesy in the category
    path('navesy/category/<slug:Slug>', views.navesCategory, name='navesCategory'),
    path('navesy/<slug:Slug>', views.navesDetails, name='navesDetails'),


    path('zvonok', views.obratniyZvonok, name="obratniyZvonok"),


    path('contacts', views.contacts, name="contacts"),
    path('pricelist', views.pricelist, name="pricelist"),
    
    path('foto-raboty/', views.portfolio, name="portfolio"),
    path('foto-raboty/<slug:Slug>', views.portfolioDetails, name='portfolioDetails'),
    


    # path('faq', sourceviews.FAQs, name="faq"),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
