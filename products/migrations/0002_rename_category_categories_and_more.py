# Generated by Django 4.2.5 on 2023-09-30 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
        migrations.RenameModel(
            old_name='Subcategory',
            new_name='Subcategories',
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Categories', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategories',
            options={'verbose_name': 'Subcategories', 'verbose_name_plural': 'Subcategories'},
        ),
    ]