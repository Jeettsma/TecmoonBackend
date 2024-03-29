# Generated by Django 4.2.2 on 2023-07-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_delete_pegatina'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_celulare',
            name='clase',
            field=models.CharField(choices=[('notebook', 'Notebook'), ('pc', 'PC'), ('celular', 'Celular')], default='celular', max_length=20),
        ),
        migrations.AddField(
            model_name='producto_notebook',
            name='clase',
            field=models.CharField(choices=[('notebook', 'Notebook'), ('pc', 'PC'), ('celular', 'Celular')], default='notebook', max_length=20),
        ),
        migrations.AddField(
            model_name='producto_pc',
            name='clase',
            field=models.CharField(choices=[('notebook', 'Notebook'), ('pc', 'PC'), ('celular', 'Celular')], default='pc', max_length=20),
        ),
    ]
