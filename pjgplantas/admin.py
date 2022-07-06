from django.contrib import admin

from pjgplantas.models import Curtida, ItensCarrinho, PedidoCarrinho, Planta, TipoUsuario, Usuario

admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Planta)
admin.site.register(PedidoCarrinho)
admin.site.register(ItensCarrinho)
admin.site.register(Curtida)

