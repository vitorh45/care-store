from django.db import models
from django.template.defaultfilters import slugify
from django.utils.formats import number_format
from os.path import splitext, split, join
from datetime import datetime
from autoslug import AutoSlugField


def slugify_file_name(instance, filename):

    path, file_name = split(filename)    
    file_name, ext = splitext(file_name)
    return '/'.join(['uploads/', slugify(file_name)+ext])


class Category(models.Model):

    name = models.CharField('Nome', max_length=100, unique=True)
    slug = AutoSlugField('Slug', populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Product(models.Model):

    category = models.ForeignKey('Category', verbose_name='Categoria')
    name = models.CharField('Nome',max_length=100,unique=True)
    slug = AutoSlugField('Slug', populate_from='name')
    description = models.TextField('Descricao')    
    main_image = models.ImageField('Imagem principal', upload_to=slugify_file_name, max_length=400)    
    price = models.DecimalField('Preco', max_digits=10, decimal_places=2)
    hit_count = models.IntegerField('Contador de Visitas', default=0)
    is_home_showcase = models.BooleanField('Destaque na página inicial?',default=False)
    is_used = models.BooleanField('Este é um produto usado?',default=False)
    is_active = models.BooleanField('Esta ativo?',default=True)
    date_creation = models.DateTimeField('Data de criacao',auto_now_add=True)
    date_update = models.DateTimeField('Data alreracao',auto_now=True,editable=False)        
    has_option = models.BooleanField("Este produto possui opção?", default=True)
    
    def __str__(self):
        return self.name

    class Meta:        
        ordering = ['-date_creation']
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
    @property
    def valor_formatado_br(self):        
        return number_format(self.price, 2) 
        

class Option(models.Model):

    product = models.ForeignKey('Product', verbose_name='Produto', related_name='opcoes')
    name = models.CharField('Opção',max_length=2, default="U", help_text='Exemplo: G, M, P, Vermelho')
        
    def __str__(self):
        return self.name
    
    def save(self):
       self.name = self.name.upper()
       super(Option, self).save()


class ProductImage(models.Model):

    product = models.ForeignKey('Product', verbose_name='Produto')
    name = models.CharField('Nome da imagem', max_length=100)
    image = models.ImageField('Imagem', upload_to=slugify_file_name, max_length=400)
    
    def __str__(self):
        return self.name