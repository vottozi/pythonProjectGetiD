# Generated by Django 4.1.3 on 2022-12-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0003_alter_tvparser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvparser',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
