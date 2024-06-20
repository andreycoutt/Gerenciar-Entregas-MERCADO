from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import CadastrarCliente, CadastrarEntrega

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CadastrarClienteCreate(LoginRequiredMixin, CreateView):
  login_url = reverse_lazy('login')
  model = CadastrarCliente
  fields = '__all__'
  template_name = 'cadastros/form.html'
  success_url = reverse_lazy('listar-cliente')

def form_valid(self, form):
  form.instance.usuario = self.request.user

  url = super().form_valid(form)

  return url
  

class CadastrarEntregaCreate(LoginRequiredMixin, CreateView):
  login_url = reverse_lazy('login')
  model = CadastrarEntrega
  fields = '__all__'
  template_name = 'cadastros/form.html'
  success_url = reverse_lazy('listar-entrega')

def form_valid(self, form):
  form.instance.usuario = self.request.user

  url = super().form_valid(form)

##################### UPDATE #####################


class ClienteUpdate(LoginRequiredMixin, UpdateView):
  login_url = reverse_lazy('login')
  model = CadastrarCliente
  fields = ['nome', 'telefone', 'endereco']
  template_name = 'cadastros/formcliente.html'
  success_url = reverse_lazy('listar-cliente')


class EntregaUpdate(LoginRequiredMixin, UpdateView):
  login_url = reverse_lazy('login')
  model = CadastrarEntrega
  fields = '__all__'
  template_name = 'cadastros/formentrega.html'
  success_url = reverse_lazy('listar-entrega')


##################### DELETE #####################


class ClienteDelete(LoginRequiredMixin, DeleteView):
  login_url = reverse_lazy('login')
  model = CadastrarCliente
  template_name = 'cadastros/form-excluir.html'
  success_url = reverse_lazy('listar-cliente')


class EntregaDelete(LoginRequiredMixin, DeleteView):
  login_url = reverse_lazy('login')
  model = CadastrarEntrega
  template_name = 'cadastros/form-excluir2.html'
  success_url = reverse_lazy('listar-entrega')


##################### LISTVIEWS #####################


class ClienteList(LoginRequiredMixin, ListView):
  model = CadastrarCliente
  template = 'cadastros/listar-cliente.html'


class EntregaList(LoginRequiredMixin, ListView):
  model = CadastrarEntrega
  template = 'cadastros/listar-entrega.html'
