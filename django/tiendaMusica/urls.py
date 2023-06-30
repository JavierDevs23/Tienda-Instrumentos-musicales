"""tiendaMusica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('acerca/', include('acerca.urls')),
    path('contacto/', include('contacto.urls')),
    path('despacho/', include('despacho.urls')),
    path('ingresar/', include('ingresar.urls')),
    path('metodospago/', include('metodospago.urls')),
    path('olvideC/', include('olvideC.urls')),
    path('politicaprivacidad/', include('politicaprivacidad.urls')),
    path('PreguntasFrec/', include('PreguntasFrec.urls')),
    path('productos/', include('productos.urls')),
    path('registrarse/', include('registrarse.urls')),
    path('retiro/', include('retiro.urls')),
    path('tablacarro/', include('tablacarro.urls')),
    path('terminosCondiciones/', include('terminosCondiciones.urls'))
]
