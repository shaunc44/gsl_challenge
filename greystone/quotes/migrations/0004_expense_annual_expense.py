# Generated by Django 2.0.5 on 2018-08-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20180806_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='annual_expense',
            field=models.PositiveIntegerField(default=0, verbose_name='annual Expense'),
        ),
    ]
