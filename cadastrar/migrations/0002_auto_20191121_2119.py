# Generated by Django 2.2.4 on 2019-11-22 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Analises',
            new_name='Clientes',
        ),
        migrations.AlterModelOptions(
            name='clientes',
            options={'verbose_name_plural': 'Clientes'},
        ),
    ]