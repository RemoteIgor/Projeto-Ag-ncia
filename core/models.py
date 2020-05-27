import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('criação', auto_now_add=True)
    modificado = models.DateField('Atualização',auto_now=True)
    ativo = models.BooleanField('Ativo?',default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICE = (
        ('shopping-cart', 'Carrinho de mercado'),
        ('laptop', 'Computador'),
        ('lock', 'Cadeado'),
    )
    servico = models.CharField('Serviço', max_length=30)
    descricao = models.TextField('Descrição',max_length=300)
    icone = models.CharField('Icone',max_length=15, choices=ICONE_CHOICE)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

class Categoria(Base):
    categoria = models.CharField('Categoria de serviço', max_length=20)

    class Meta:
        verbose_name = 'Categoria '
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.categoria

class Portfolio(Base):
    id = models.AutoField('Id', primary_key=True)
    nome = models.CharField('Nome do projeto', max_length=50)
    cliente = models.CharField('Cliente', max_length=20)
    descricao = models.TextField('Descrição do projeto', max_length=300)
    categoria = models.ForeignKey('core.Categoria', verbose_name='Categoria', on_delete=models.CASCADE)
    imagem = StdImageField('Imagem do projeto', upload_to=get_file_path, variations={'thumb': {'width': 400, 'height': 300, 'crop': True}})

    class Meta:
        verbose_name = 'Portfólio '
        verbose_name_plural = 'Portfólios'

    def __str__(self):
        return self.nome

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=20)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Colaborador(Base):
    nome = models.CharField('Nome', max_length=20)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    imagem = StdImageField('Foto', upload_to=get_file_path, variations={'thumb': {'width': 500, 'height': 500, 'crop': True}})
    twitter = models.CharField('Twitter', max_length=100, default='#')
    facebook = models.CharField('Twitter', max_length=100, default='#')
    linkedin = models.CharField('Twitter', max_length=100, default='#')

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome



