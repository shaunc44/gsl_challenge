# Generated by Django 2.0.5 on 2018-08-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0012_auto_20180809_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='debt_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='debt Rate'),
        ),
    ]
