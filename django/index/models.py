from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria  = models.AutoField(db_column='idcategoria', primary_key=True) 
    categoria     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)
    
class Producto(models.Model):
    codigo_producto  = models.CharField(primary_key=True, max_length=8)
    id_categoria     = models.ForeignKey('Categoria' ,on_delete=models.CASCADE, db_column='idcategoria') 
    nombre           = models.CharField(max_length=30)
    imagen           = models.ImageField(upload_to='image/')
    referencia       = models.IntegerField(blank=False, null=False)
    color            = models.CharField(max_length=30)
    cantidad         = models.IntegerField(blank=False, null=False)
    descripcion      = models.TextField(blank=False, null=False)
    origen           = models.CharField(max_length=30)
    serie            = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.nombre)
    
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True) 
    genero    = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return str(self.genero)
    
class Persona(models.Model):
    codigo_persona = models.CharField(primary_key=True, max_length=10)
    nombres        = models.CharField(max_length=40)
    apellidos      = models.CharField(max_length=40)    
    id_genero      = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    nombre_usuario = models.CharField(max_length=60)
    email          = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    telefono       = models.CharField(max_length=45)
    contrasena     = models.CharField(max_length=24)
    
    def __str__(self):
        return str(self.nombres)+' '+str(self.apellidos)