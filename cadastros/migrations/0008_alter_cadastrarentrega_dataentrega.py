# Generated by Django 5.0.2 on 2024-05-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_alter_cadastrarentrega_dataentrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrarentrega',
            name='dataentrega',
            field=models.DateField(verbose_name='Data da Entrega'),
        ),
    ]
