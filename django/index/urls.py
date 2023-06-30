from django.urls import path
from . import views

urlpatterns = [
    # inicio proyecto.
    path('',views.index,name ='index'),
    # Menu
    path('menu',views.menu,name ='menu'),
    # gestor producto.
    path('gestor',views.gestor,name ='gestor'),
    path('listaproducto',views.listaProducto,name ='listaproducto'),
    path('listacategoria',views.listaCategoria,name ='listacategoria'),
    path('gestoradd',views.agregarProducto,name ='gestoradd'),
    path('eliminarproducto/<str:pk>',views.eliminarProducto,name ='eliminarproducto'),
    path('buscarproducto/<str:pk>',views.buscarProducto,name ='buscarproducto'),
    path('actualizarproducto',views.actualizarProducto,name ='actualizarproducto'),
    # gestor usuario.
    path('gestorpersona',views.gestorPersona,name ='gestorpersona'),
    path('listapersona',views.listaPersona,name ='listapersona'),
    path('listagenero',views.listaGenero,name ='listagenero'),
    path('agregarpersona',views.agregarPersona,name ='agregarpersona'),
    path('eliminarpersona/<str:pk>',views.eliminarPersona,name ='eliminarpersona'),
    path('buscarpersona/<str:pk>',views.buscarPersona,name ='buscarpersona'),
    path('actualizarpersona',views.actualizarPersona,name ='actualizarpersona'),
]

