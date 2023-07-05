from django.urls import path
from .views import home,Notebook,pc,modal,formulario,Celulares,agregar,listar,registrar, comprar
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('Notebook/', Notebook, name='Notebook'),
    path('pc/', pc, name='PC'),
    path('modal/', modal, name='modal'),
    path('formulario/', formulario, name='formulario'),
    path('Celulares/', Celulares, name='Celulares'),
    path('agregar/', agregar, name='agregar'),
    path('listar/', listar, name='listar'),
    path('modificar/pc/<int:id>/', views.modificar_pc, name='modificar_pc'),
    path('modificar/notebook/<int:id>/', views.modificar_notebook, name='modificar_notebook'),
    path('modificar/celular/<int:id>/', views.modificar_celular, name='modificar_celular'),
    path('eliminar/pc/<int:id>/', views.eliminar_pc, name='eliminar_pc'),
    path('eliminar/notebook/<int:id>/', views.eliminar_notebook, name='eliminar_notebook'),
    path('eliminar/celular/<int:id>/', views.eliminar_celular, name='eliminar_celular'),
    path('registrar/', registrar, name='registrar'),
    path('comprar/', comprar, name='comprar'),
    path('notebooks/<int:notebook_id>/', views.notebook_detail, name='notebook_detail'),
    path('pcs/<int:pc_id>/', views.pc_detail, name='pc_detail'),
    path('celulares/<int:celular_id>/', views.celular_detail, name='celular_detail'),
    path('agregar_carro/<int:producto_id>/<str:tipo_producto>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_carro/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('sumar_carro/<int:producto_id>/', views.sumar_cantidad, name='sumar_cantidad'),
    path('restar_carro/<int:producto_id>/', views.restar_cantidad, name='restar_cantidad'),
    path('vaciar_carro/', views.vaciar_carrito, name='vaciar_carrito'),
    path('ver_carro/', views.ver_carrito, name='ver_carrito'),
    path('productos/notebooks/', views.listar_notebooks, name='listar_notebooks'),
    path('productos/pcs/', views.listar_pcs, name='listar_pcs'),
    path('productos/celulares/', views.listar_celulares, name='listar_celulares'),
    
    
    

   
]