# Generated by Django 5.0.2 on 2024-05-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrarcliente',
            name='cpf',
            field=models.IntegerField(unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cadastrarentrega',
            name='volumeextra',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Volume Extra'),
        ),
    ]
