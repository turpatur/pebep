# Generated by Django 5.1.2 on 2024-10-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo_diskon', '0008_alter_discentry_code_alter_discentry_resto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discentry',
            name='code',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]