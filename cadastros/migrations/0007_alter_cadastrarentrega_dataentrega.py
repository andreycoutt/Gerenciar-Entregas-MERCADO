# Generated by Django 5.0.2 on 2024-05-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_remove_cadastrarcliente_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrarentrega',
            name='dataentrega',
            field=models.DateTimeField(verbose_name='Data da Entrega'),
        ),
    ]
