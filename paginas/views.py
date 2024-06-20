from django .views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
class IndexView(LoginRequiredMixin, TemplateView):
  login_url = reverse_lazy('login')
  template_name = "paginas/index.html"
  
# class CadastrarClienteView(TemplateView):
#  template_name = 'paginas/cadastrarcliente.html'

# class ListarClienteView(TemplateView):
#  template_name = 'paginas/listarentregas.html'

class CadastrarClienteView(TemplateView):
  template_name = "paginas/cadastrarcliente.html"

class ListarClienteView(TemplateView):
  template_name = "paginas/listarcliente.html"

class CadastrarEntregaView(TemplateView):
  template_name = "paginas/cadastrarentrega.html"

class ListarEntregasView(TemplateView):
  template_name = "paginas/listarentrega.html"