from django.db import models



class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

 
    
class transicione(models.Model):
    nombre =  models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="transiciones", null = True)

    def __str__(self):
        return self.nombre  
     
class producto_notebook(models.Model):
    CLASE_CHOICES = (
        ('notebook', 'Notebook'),
        ('pc', 'PC'),
        ('celular', 'Celular'),
    )

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos_notebooks", null=True)
    clase = models.CharField(max_length=20, choices=CLASE_CHOICES, default='notebook')

    def __str__(self):
        return self.nombre


class producto_pc(models.Model):
    CLASE_CHOICES = (
        ('notebook', 'Notebook'),
        ('pc', 'PC'),
        ('celular', 'Celular'),
    )

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos_pcs", null=True)
    clase = models.CharField(max_length=20, choices=CLASE_CHOICES, default='pc')

    def __str__(self):
        return self.nombre


class producto_celulare(models.Model):
    CLASE_CHOICES = (
        ('notebook', 'Notebook'),
        ('pc', 'PC'),
        ('celular', 'Celular'),
    )

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos_celulares", null=True)
    clase = models.CharField(max_length=20, choices=CLASE_CHOICES, default='celular')

    def __str__(self):
        return self.nombre

    

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],    
    [2, "sugerencia"],
    [3, "felicitaciones"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)    
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
