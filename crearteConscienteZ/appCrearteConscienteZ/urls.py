from os import name
from django.urls import  path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore


from appCrearteConscienteZ import views

urlpatterns = [
    path('', views.home, name="Home")
]

urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)