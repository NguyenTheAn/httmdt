# Generated by Django 3.0.5 on 2021-06-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, db_column='Image', max_length=255, null=True),
        ),
    ]
