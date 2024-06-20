from django.urls import path
from .views import CadastrarClienteCreate, CadastrarEntregaCreate
from .views import ClienteUpdate, EntregaUpdate
from .views import ClienteDelete, EntregaDelete
from .views import ClienteList, EntregaList

urlpatterns = [
   path('cadastrar/cliente/', CadastrarClienteCreate.as_view(), name='cadastrar-cliente'),
   path('cadastrar/entrega/', CadastrarEntregaCreate.as_view(), name='cadastrar-entrega'),

   path('editar/cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar-cliente'),
   path('editar/entrega/<int:pk>/', EntregaUpdate.as_view(), name='editar-entrega'),

   path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name='excluir-cliente'),
   path('excluir/entrega/<int:pk>/', EntregaDelete.as_view(), name='excluir-entrega'),

   path('listar/cliente/', ClienteList.as_view(), name='listar-cliente'),
   path('listar/entrega/', EntregaList.as_view(), name='listar-entrega'),
   
]