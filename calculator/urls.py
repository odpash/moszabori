from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .sourceviews import profnastil, rabitsa, metal, boarder


app_name = 'calc'

urlpatterns = [
    path('', profnastil.main, name='calculator'),
    path('/calc-profnastil', profnastil.main, name="profnastil"),
    path('/calc-rabitsa', rabitsa.main, name="rabitsa"),
    path('/calc-metal', metal.main, name="metal"),
    path('/calc-boarder', boarder.main, name="boarder"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
