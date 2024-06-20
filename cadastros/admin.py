from django.contrib import admin
from .models import CadastrarCliente, CadastrarEntrega

# Register your models here.
admin.site.register(CadastrarCliente)
admin.site.register(CadastrarEntrega)
