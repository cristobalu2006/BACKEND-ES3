from django.db import models



class Autor(models.Model):

    nombre = models.CharField(null=False, max_length=200)
    nacionalidad = models.CharField(null=False, max_length=200)
    anio_nacimiento = models.PositiveIntegerField(null=False)

    class Meta:
        verbose_name_plural = 'Autores'
        ordering = ['nombre']
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} Nacionalidad: {self.nacionalidad} Año de nacimiento: {self.anio_nacimiento}'


class Libro(models.Model):

    titulo = models.CharField(null=False, max_length=200)
    isbn = models.CharField(unique=True, null=False, max_length=20)
    anio_publicacion = models.PositiveIntegerField(null=False)

    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Libros'
        ordering = ['anio_publicacion']
    
    def __str__(self) -> str:
        return f'Título: {self.titulo} ISBN: {self.isbn} Año de publicación: {self.anio_publicacion} ID de Autor: {self.autor_id}'
