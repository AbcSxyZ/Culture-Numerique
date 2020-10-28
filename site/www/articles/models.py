from django.db import models

# Create your models here.

class Commentary(models.Model):
    username = models.CharField(max_length=50, 
            verbose_name="Pseudo")
    comment = models.TextField(verbose_name="Commentaire")
    article = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)

