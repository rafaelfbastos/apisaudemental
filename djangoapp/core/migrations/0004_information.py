# Generated by Django 4.2.5 on 2023-09-30 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_contacts_options_alter_phones_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('text', models.TextField(verbose_name='Texto')),
                ('img', models.ImageField(null=True, upload_to='img/', verbose_name='imagem')),
                ('themeColor', models.CharField(null=True, verbose_name='cor')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Informação',
                'verbose_name_plural': 'Informações',
            },
        ),
    ]
