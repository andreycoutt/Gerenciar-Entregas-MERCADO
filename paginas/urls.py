from django.urls import path
from .views import IndexView, CadastrarClienteView, ListarClienteView, CadastrarEntregaView, ListarEntregasView

urlpatterns = [
  # path ('url/', MinhaView.as_view(), name='nomeurl')
  path('', IndexView.as_view(), name='index'),
  path('cadastrarcliente/', CadastrarClienteView.as_view(), name='cadastrarcliente'),
  path('listarcliente/', ListarClienteView.as_view(), name='listarcliente'),
  path('cadastrarentrega/', CadastrarEntregaView.as_view(), name='cadastrarentrega'),
  path('listarentrega/', ListarEntregasView.as_view(), name='listarentrega'),
]