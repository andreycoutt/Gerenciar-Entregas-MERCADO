# Generated by Django 5.0.2 on 2024-05-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_alter_cadastrarentrega_volumeextra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastrarcliente',
            name='id',
        ),
        migrations.AlterField(
            model_name='cadastrarcliente',
            name='cpf',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='CPF'),
        ),
    ]
