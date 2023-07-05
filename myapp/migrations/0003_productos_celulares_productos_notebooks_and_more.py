# Generated by Django 4.2.2 on 2023-06-12 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='productos_celulares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='productos_celulares')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.marca')),
            ],
        ),
        migrations.CreateModel(
            name='productos_notebooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='productos_notebooks')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.marca')),
            ],
        ),
        migrations.CreateModel(
            name='productos_pcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='productos_pcs')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.marca')),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
