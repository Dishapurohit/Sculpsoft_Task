# Generated by Django 3.0.7 on 2020-07-10 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0015_auto_20200710_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
