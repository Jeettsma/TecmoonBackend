# Generated by Django 4.2.2 on 2023-06-15 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_transicione_delete_logo_transicione'),
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='logos')),
            ],
        ),
    ]