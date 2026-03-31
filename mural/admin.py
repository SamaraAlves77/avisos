from django.contrib import admin
from .models import Categoria, Aviso

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Exibe o nome da categoria na listagem
    list_display = ('id', 'nome')
    # Permite pesquisar categorias pelo nome
    search_fields = ('nome',)


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    # Colunas que aparecem na tabela de avisos
    list_display = ('titulo', 'categoria', 'data_criacao')
    
    # Filtros laterais para facilitar a navegação
    list_filter = ('categoria', 'data_criacao')
    
    # Barra de busca que procura no título e no conteúdo
    search_fields = ('titulo', 'conteudo')
    
    # Define que a data de criação não pode ser editada (já que é auto_now_add)
    # mas aparecerá como campo apenas de leitura no formulário
    readonly_fields = ('data_criacao',)
    
    # Ordenação: os avisos mais recentes aparecem primeiro
    ordering = ('-data_criacao',)