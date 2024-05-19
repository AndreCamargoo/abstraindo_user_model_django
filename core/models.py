from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager

# HERDA UM USARIO MAIS BASICO SEM VARIAS FUNÇÕES
"""
class CustomUsers(AbstractBaseUser):
    pass

    def __str__(self):
        return self.email
"""


# GERENCIADO DE USARIO
class CustomUsersManager(BaseUserManager):
    use_in_migrations = True

    # sobreescrevendo o cadastro
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    # salvando o usuario comum
    def create_user(self, email, password=None, **extra_fields):
        """
        Acessar area administrativa, por padrão é False
        extra_fields.setdefault('is_staff', True)
        """

        # Usuario comum
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    # usuario administrativo
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super usuário precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super usuário precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


# HERDA A CLASSE COMPLETA
class CustomUsers(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    # definindo como irá logar
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email

    object = CustomUsersManager()

# EXEMPLO UM DE COMO CRIAR UMA CHAVE ESTRANGEIRA (NÃO IDEAL)
"""
class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=100)
    content = models.TextField('content', max_length=400)

    def __str__(self):
        return self.title
"""


# EXEMPLO DOIS DE COMO CRIAR UMA CHAVE ESTRANGEIRA (PEGANDO DE QUAL MODEL IRÁ PEGAR A CHAVE ESTRANGEIRA)
"""
class Post2(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=100)
    content = models.TextField('content', max_length=400)

    def __str__(self):
        return self.title
"""


# EXEMPLO TRÊS DE COMO CRIAR UMA CHAVE ESTRANGEIRA (MANEIRA INDICADA)
"""
class Post3(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=100)
    content = models.TextField('content', max_length=400)

    def __str__(self):
        return self.title
"""
