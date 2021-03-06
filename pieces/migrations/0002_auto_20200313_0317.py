# Generated by Django 2.1.1 on 2020-03-12 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieces', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='need',
        ),
        migrations.AlterField(
            model_name='piece',
            name='amount',
            field=models.DecimalField(decimal_places=5, default=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='piece',
            name='parent_product_code',
            field=models.BigIntegerField(),
        ),
    ]
