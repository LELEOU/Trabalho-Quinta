from django.db import models

class Category(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    limite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Limite")
    tipo = models.CharField(max_length=50, verbose_name="Tipo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created_at']

    def __str__(self):
        return self.descricao