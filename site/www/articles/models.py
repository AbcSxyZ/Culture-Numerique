from django.db import models
from django.core.mail import mail_admins

# Create your models here.

class Commentary(models.Model):
    username = models.CharField(max_length=50, 
            verbose_name="Pseudo")
    comment = models.TextField(verbose_name="Commentaire")
    article = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        msg = "Nouveau commentaire de {}:\n\n{}\n"
        msg = msg.format(self.username, self.comment)
        super().save(*args, **kwargs)
        mail_admins(subject="Nouveau commentaire", message=msg)

