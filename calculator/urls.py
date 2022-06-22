from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .sourceviews import profnastil, rabitsa, metal, boarder, navesi, news


app_name = 'calc'

urlpatterns = [
    path('', profnastil.main, name='calculator'),
    path('/calc-profnastil', profnastil.main, name="profnastil"),
    path('/calc-rabitsa', rabitsa.main, name="rabitsa"),
    path('/calc-metal', metal.main, name="metal"),
    path('/calc-boarder', boarder.main, name="boarder"),
    path('/calc-navesi', navesi.main, name="navesi"),
    path('/article1', news.main, name='article1'),
    path('/article2', news.main2, name='article2'),
    path('/article3', news.main3, name='article3'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
