from django.db import models

class Characters(models.Model):
    title = models.CharField('Назва', max_length=50)
    img = models.ImageField('Картинка')
    info = models.TextField('Інформація')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Герой'
        verbose_name_plural = 'Герої'