# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Prefetch
# Create your views here.
from models import Publicadores, Atividades
class ListaPublicadoresView(ListView):
    ## Manager padrão que retona todas as linhas da tabela all().
    #model = Publicadores
    def get_queryset(self):    
        pubs = Publicadores.objects.all().prefetch_related(Prefetch("atividades_set",queryset=Atividades.objects.filter(anomes="201710"),to_attr="some_atividades"))
        for a in pubs:
            somePhotos = a.some_atividades    
                #pubs = Publicadores.objects.all().select_related().prefetch_related('atividades_set')

        #ati = pub.atividades_set.qt_publicacoes
        #relcampos = RelatoriosCampo.objects.filter(id_publicador_id='1')
        #pub.publicadores__set.all()
        #relcampos = pub.relatorioscampo_set.all()
        #relcampos = RelatoriosCampo.objects.filter(id_publicador=pub)
        #print("queryset1",queryset)
        #queryset = queryset.values('nome','bairro','telefone2').order_by('bairro').distinct()  #not working
        #print("pub.nome",pub[0].congregacao.nome)
        #print("pub.endereco",pub[0].endereco.logradouro)
        #print("pub.grupo",pub[0].grupo.nome)
        #print("ati",pub[0].atividades_set.qt_publicacoes)
        #print("pub.nome",pub.congregacao.nome)
        #print("relcampos[0].ano....................:",relcampos[0].ano)
                                    
                                                               #telefone2notnulo not defined in field options  
        #queryset = queryset.values('nome','bairro').order_by('bairro').distinct() #workfine
            
        ##distintos -> manager que retorna colunas 'nome','telefone2','bairro'. Ordenador por bairro. E distintos
        #queryset = PublicadoresDistintos.distintos.all()
        
        ##socantegril -> manager que filtra somente bairros = Cantegril
        #queryset = Publicadores.socantegril.all().values('nome','rg','bairro').order_by('bairro').distinct()
        return a
    
def index(request):
    return render(request, 'adm/index.html') 
