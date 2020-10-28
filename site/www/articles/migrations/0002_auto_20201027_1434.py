# Generated by Django 3.1.2 on 2020-10-27 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='article',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentary',
            name='comment',
            field=models.TextField(verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Pseudo'),
        ),
    ]
