from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .sourceviews import profnastil, rabitsa


app_name = 'calc'

urlpatterns = [
    path('', profnastil.main, name='calculator'),
    path('/calc-profnastil', profnastil.main, name="profnastil"),
    path('/calc-rabitsa', rabitsa.main, name="rabitsa"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
