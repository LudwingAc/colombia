"""colombia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from col import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('municipio', views.municipio),
    path('municipio-lista', views.MunicipioList.as_view(), name='municipio_list'),
    path('municipio-detalles/<int:pk>', views.MunicipioView.as_view(), name='municipio_view'),
    path('municipio-crear', views.MunicipioCreate.as_view(), name='municipio_new'),
    path('municipio-detalles/<int:pk>', views.MunicipioView.as_view(), name='municipio_view'),
    path('municipio-editar/<int:pk>', views.MunicipioUpdate.as_view(), name='municipio_edit'),
    path('municipio-eliminar/<int:pk>', views.MunicipioDelete.as_view(), name='municipio_delete'),

    path('region-lista', views.RegionList.as_view(), name='region_list'),
    path('region-detalles/<int:pk>', views.RegionView.as_view(), name='region_view'),
    path('region-crear', views.RegionCreate.as_view(), name='region_new'),
    path('region-detalles/<int:pk>', views.RegionView.as_view(), name='region_view'),
    path('region-editar/<int:pk>', views.RegionUpdate.as_view(), name='region_edit'),
    path('region-eliminar/<int:pk>', views.RegionDelete.as_view(), name='region_delete'),

    path('logica/', views.numero, name='logica'),
    path('', views.prueba, name='index'),
    #path('colombia/', include('colombia.urls')),

]
