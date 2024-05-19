from django.contrib import admin
#from .models import Post, Post3
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsersCreateForm, CustomUsersChangeForm
from .models import CustomUsers


@admin.register(CustomUsers)
class CustomUsersAdmin(UserAdmin):
    add_form = CustomUsersCreateForm
    form = CustomUsersChangeForm
    model = CustomUsers

    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')})
    )

"""
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Post3)
class Post3Admin(admin.ModelAdmin):
    list_display = ('title', '_author')
    # NÃO PERMITINDO QUE O USARIO INFORME OUTRO USUARIO NA CRIAÇÃO DO POST (PEGAR O MESMO LOGADO)
    exclude = ['author',]

    # CRIANDO UMA FUNÇÃO PARA APRESENTAR NOME COMPLETO NO PAINEL DE ADMINISTRAÇÃO
    def _author(self, instance):
        return f'{instance.author.get_full_name()}'

    # MOSTRANDO SOMENTE OS DADOS CRIADOS PELO USUARIO, IMPEDINDO DE VER OUTROS DADOS CRIADOS
    def get_queryset(self, request):
        qs = super(Post3Admin, self).get_queryset(request)
        return qs.filter(author=request.user)

    # QUANDO SALVAR PEGAR O USAURIO DA SESSÃO
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
"""
